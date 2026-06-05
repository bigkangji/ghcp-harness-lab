import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
