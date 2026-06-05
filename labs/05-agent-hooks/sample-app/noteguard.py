"""A tiny markdown note CLI for the Agent Hooks lab."""

import argparse
import os
from pathlib import Path
from typing import Optional

DEFAULT_NOTES_FILE = Path("notes.md")


def resolve_notes_file() -> Path:
    """Return the notes file path, honoring NOTEGUARD_FILE when set."""
    override = os.environ.get("NOTEGUARD_FILE")
    if override:
        return Path(override)
    return DEFAULT_NOTES_FILE


def add_note(text: str, notes_file: Optional[Path] = None) -> None:
    note = text.strip()
    if not note:
        raise ValueError("note text cannot be empty")

    path = notes_file or resolve_notes_file()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"- {note}\n")


def list_notes(notes_file: Optional[Path] = None) -> list[str]:
    path = notes_file or resolve_notes_file()
    if not path.exists():
        return []

    notes: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            notes.append(stripped[2:])
    return notes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="noteguard")
    subcommands = parser.add_subparsers(dest="command", required=True)

    add_parser = subcommands.add_parser("add", help="append a note")
    add_parser.add_argument("text", help="note text to append")

    subcommands.add_parser("list", help="list saved notes")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        try:
            add_note(args.text)
        except ValueError as error:
            parser.error(str(error))
        return 0

    if args.command == "list":
        for index, note in enumerate(list_notes(), start=1):
            print(f"{index}. {note}")
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())