import os
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TodoLine:
    source_index: int
    done: bool
    text: str


def todo_path():
    return Path(os.environ.get("MDTODO_FILE", "./tasks.md"))


def read_lines(path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as file:
        return file.read().splitlines(keepends=True)


def write_lines(path, lines):
    with path.open("w", encoding="utf-8", newline="") as file:
        file.write("".join(lines))


def trailing_newline(line):
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n"):
        return "\n"
    if line.endswith("\r"):
        return "\r"
    return ""


def parse_todo_line(index, line):
    body = line.rstrip("\n")
    if body.endswith("\r"):
        body = body[:-1]
    if body.startswith("- [ ] "):
        return TodoLine(index, False, body[len("- [ ] "):])
    if body.startswith("- [x] "):
        return TodoLine(index, True, body[len("- [x] "):])
    return None


def todo_lines(lines):
    parsed = []
    for index, line in enumerate(lines):
        todo = parse_todo_line(index, line)
        if todo is not None:
            parsed.append(todo)
    return parsed


def incomplete_todos(lines):
    return [todo for todo in todo_lines(lines) if not todo.done]


def command_add(text):
    path = todo_path()
    lines = read_lines(path)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] = lines[-1] + "\n"
    lines.append(f"- [ ] {text}\n")
    write_lines(path, lines)
    number = len(incomplete_todos(lines))
    print(f"Added #{number}: {text}")
    return 0


def command_list():
    lines = read_lines(todo_path())
    for number, todo in enumerate(incomplete_todos(lines), start=1):
        print(f"- [ ] {number}. {todo.text}")
    return 0


def invalid_number(raw_number):
    print(f"Invalid todo number: {raw_number}", file=sys.stderr)
    return 1


def command_done(raw_number):
    try:
        number = int(raw_number)
    except ValueError:
        return invalid_number(raw_number)

    if number < 1:
        return invalid_number(raw_number)

    path = todo_path()
    lines = read_lines(path)
    incomplete = incomplete_todos(lines)
    if number > len(incomplete):
        return invalid_number(raw_number)

    todo = incomplete[number - 1]
    original_line = lines[todo.source_index]
    lines[todo.source_index] = f"- [x] {todo.text}{trailing_newline(original_line)}"
    write_lines(path, lines)
    print(f"Done: {todo.text}")
    return 0


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) >= 2 and argv[0] == "add":
        return command_add(" ".join(argv[1:]))
    if len(argv) == 1 and argv[0] == "list":
        return command_list()
    if len(argv) == 2 and argv[0] == "done":
        return command_done(argv[1])

    print("Usage: mdtodo add TEXT | list | done N", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
