import os
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import goalkeeper

ROOT = Path(__file__).resolve().parents[1]


class GoalkeeperCliTest(unittest.TestCase):
    def run_cli(self, *args, goal_file=None):
        env = os.environ.copy()
        if goal_file is not None:
            env["GOALKEEPER_FILE"] = str(goal_file)
        return subprocess.run(
            [sys.executable, "-m", "goalkeeper", *args],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_add_stores_pending_goal(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            goal_file = Path(temp_dir) / "goals.md"
            result = self.run_cli("add", "ship lab 06", goal_file=goal_file)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(goal_file.read_text(encoding="utf-8"), "- [ ] ship lab 06\n")

    def test_list_prints_numbered_goals(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            goal_file = Path(temp_dir) / "goals.md"
            goal_file.write_text("- [ ] write tests\n- [x] update docs\n", encoding="utf-8")

            result = self.run_cli("list", goal_file=goal_file)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "1. [ ] write tests\n2. [x] update docs\n")

    def test_done_marks_nth_goal_done(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            goal_file = Path(temp_dir) / "goals.md"
            goal_file.write_text("- [ ] write tests\n- [ ] update docs\n", encoding="utf-8")

            result = self.run_cli("done", "2", goal_file=goal_file)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                goal_file.read_text(encoding="utf-8"),
                "- [ ] write tests\n- [x] update docs\n",
            )

    def test_empty_goal_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            goal_file = Path(temp_dir) / "goals.md"
            result = self.run_cli("add", "   ", goal_file=goal_file)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("empty", result.stderr.lower())
            self.assertFalse(goal_file.exists())

    def test_web_app_lists_adds_and_completes_goals(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            goal_file = Path(temp_dir) / "goals.md"
            goal_file.write_text("- [ ] write tests\n", encoding="utf-8")
            server = goalkeeper.create_server(("127.0.0.1", 0), goal_file)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()

            try:
                base_url = f"http://127.0.0.1:{server.server_port}"
                page = urlopen(base_url, timeout=5).read().decode("utf-8")
                self.assertIn("write tests", page)
                self.assertIn("Goalkeeper", page)

                add_body = urlencode({"text": "ship web ui"}).encode("utf-8")
                add_request = Request(base_url + "/add", data=add_body, method="POST")
                urlopen(add_request, timeout=5).read()
                self.assertEqual(
                    goal_file.read_text(encoding="utf-8"),
                    "- [ ] write tests\n- [ ] ship web ui\n",
                )

                done_body = urlencode({"number": "2"}).encode("utf-8")
                done_request = Request(base_url + "/done", data=done_body, method="POST")
                urlopen(done_request, timeout=5).read()
                self.assertEqual(
                    goal_file.read_text(encoding="utf-8"),
                    "- [ ] write tests\n- [x] ship web ui\n",
                )
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
