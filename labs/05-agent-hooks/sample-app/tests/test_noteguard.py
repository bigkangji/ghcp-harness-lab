import os
import tempfile
import unittest
from pathlib import Path

import noteguard


class NoteGuardTest(unittest.TestCase):
    def test_add_note_appends_markdown_list_item(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            notes_file = Path(tmpdir) / "notes.md"

            noteguard.add_note("first note", notes_file)
            noteguard.add_note("second note", notes_file)

            self.assertEqual(
                notes_file.read_text(encoding="utf-8"),
                "- first note\n- second note\n",
            )

    def test_list_notes_returns_saved_notes_without_markers(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            notes_file = Path(tmpdir) / "notes.md"
            notes_file.write_text("- first note\n- second note\n", encoding="utf-8")

            self.assertEqual(noteguard.list_notes(notes_file), ["first note", "second note"])

    def test_add_note_rejects_empty_text(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            notes_file = Path(tmpdir) / "notes.md"

            with self.assertRaises(ValueError):
                noteguard.add_note("   ", notes_file)

            self.assertFalse(notes_file.exists())

    def test_resolve_notes_file_honors_environment_override(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            expected = Path(tmpdir) / "custom.md"
            old_value = os.environ.get("NOTEGUARD_FILE")
            os.environ["NOTEGUARD_FILE"] = str(expected)
            try:
                self.assertEqual(noteguard.resolve_notes_file(), expected)
            finally:
                if old_value is None:
                    os.environ.pop("NOTEGUARD_FILE", None)
                else:
                    os.environ["NOTEGUARD_FILE"] = old_value


if __name__ == "__main__":
    unittest.main()