"""Goalkeeper todo app for lab 06."""

from __future__ import annotations

from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import sys
from pathlib import Path
from urllib.parse import parse_qs


DEFAULT_GOALS_FILE = "goals.md"


def goals_path() -> Path:
    return Path(os.environ.get("GOALKEEPER_FILE", DEFAULT_GOALS_FILE))


def read_goals(path: Path) -> list[tuple[bool, str]]:
    if not path.exists():
        return []

    goals: list[tuple[bool, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("- [ ] "):
            goals.append((False, line[6:]))
        elif line.startswith("- [x] "):
            goals.append((True, line[6:]))
    return goals


def write_goals(path: Path, goals: list[tuple[bool, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"- [{'x' if done else ' '}] {text}\n" for done, text in goals]
    path.write_text("".join(lines), encoding="utf-8")


def add_goal(path: Path, text: str) -> int:
    goal = text.strip()
    if not goal:
        print("goal cannot be empty", file=sys.stderr)
        return 2

    goals = read_goals(path)
    goals.append((False, goal))
    write_goals(path, goals)
    return 0


def list_goals(path: Path) -> int:
    for index, (done, text) in enumerate(read_goals(path), start=1):
        marker = "x" if done else " "
        print(f"{index}. [{marker}] {text}")
    return 0


def complete_goal(path: Path, number_text: str) -> int:
    try:
        number = int(number_text)
    except ValueError:
        print("goal number must be an integer", file=sys.stderr)
        return 2

    goals = read_goals(path)
    if number < 1 or number > len(goals):
        print("goal number is out of range", file=sys.stderr)
        return 2

    _, text = goals[number - 1]
    goals[number - 1] = (True, text)
    write_goals(path, goals)
    return 0


def render_page(path: Path) -> str:
    goals = read_goals(path)
    items = []
    for index, (done, text) in enumerate(goals, start=1):
        checked_class = " done" if done else ""
        safe_text = escape(text)
        action = "<span class='badge'>Done</span>" if done else (
            f"<form action='/done' method='post'>"
            f"<input type='hidden' name='number' value='{index}'>"
            "<button type='submit'>Complete</button>"
            "</form>"
        )
        items.append(
            f"<li class='todo{checked_class}'>"
            f"<span class='mark'>{'x' if done else ''}</span>"
            f"<span class='text'>{safe_text}</span>"
            f"{action}"
            "</li>"
        )

    todo_items = "\n".join(items) or "<li class='empty'>No todos yet</li>"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Goalkeeper Todo</title>
  <style>
    :root {{ color-scheme: light; --ink: #202018; --paper: #f8f4ea; --line: #d8cfbd; --accent: #1f7a68; --sun: #f0b43c; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; min-height: 100vh; background: var(--paper); color: var(--ink); font-family: Georgia, 'Times New Roman', serif; }}
    main {{ width: min(720px, calc(100% - 32px)); margin: 0 auto; padding: 56px 0; }}
    header {{ display: flex; align-items: end; justify-content: space-between; gap: 20px; border-bottom: 2px solid var(--ink); padding-bottom: 18px; }}
    h1 {{ margin: 0; font-size: clamp(2.2rem, 8vw, 5rem); line-height: .85; letter-spacing: 0; }}
    .count {{ background: var(--sun); border: 2px solid var(--ink); padding: 8px 12px; font-weight: 700; white-space: nowrap; }}
    .add {{ display: grid; grid-template-columns: 1fr auto; gap: 10px; margin: 28px 0; }}
    input[type='text'] {{ min-width: 0; border: 2px solid var(--ink); background: #fffdf7; padding: 14px 16px; font: inherit; font-size: 1.05rem; }}
    button {{ border: 2px solid var(--ink); background: var(--accent); color: white; padding: 12px 16px; font: inherit; font-weight: 700; cursor: pointer; }}
    button:hover {{ filter: brightness(.92); }}
    ul {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 10px; }}
    .todo {{ display: grid; grid-template-columns: 34px 1fr auto; align-items: center; gap: 12px; background: #fffdf7; border: 2px solid var(--line); padding: 12px; }}
    .mark {{ width: 28px; height: 28px; display: grid; place-items: center; border: 2px solid var(--ink); font-weight: 700; font-family: ui-monospace, Menlo, monospace; }}
    .todo.done .text {{ text-decoration: line-through; color: #786f61; }}
    .badge {{ border: 2px solid var(--line); padding: 8px 10px; color: #786f61; font-weight: 700; }}
    .empty {{ border: 2px dashed var(--line); padding: 24px; text-align: center; color: #786f61; }}
    @media (max-width: 560px) {{ header, .add, .todo {{ grid-template-columns: 1fr; display: grid; align-items: stretch; }} .todo {{ grid-template-columns: 34px 1fr; }} .todo form, .badge {{ grid-column: 1 / -1; }} }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Goalkeeper</h1>
      <div class="count">{len(goals)} todo{'s' if len(goals) != 1 else ''}</div>
    </header>
    <form class="add" action="/add" method="post">
      <input type="text" name="text" placeholder="Add a todo" autofocus>
      <button type="submit">Add</button>
    </form>
    <ul>{todo_items}</ul>
  </main>
</body>
</html>"""


def create_server(address: tuple[str, int], path: Path) -> HTTPServer:
    goal_file = Path(path)

    class GoalkeeperHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if self.path != "/":
                self.send_error(404)
                return
            self.respond_html(render_page(goal_file))

        def do_POST(self) -> None:
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8")
            form = parse_qs(body)

            if self.path == "/add":
                add_goal(goal_file, form.get("text", [""])[0])
                self.redirect_home()
                return
            if self.path == "/done":
                complete_goal(goal_file, form.get("number", [""])[0])
                self.redirect_home()
                return

            self.send_error(404)

        def respond_html(self, html: str) -> None:
            body = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def redirect_home(self) -> None:
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()

        def log_message(self, format: str, *args: object) -> None:
            return

    return HTTPServer(address, GoalkeeperHandler)


def serve(path: Path, host: str = "127.0.0.1", port: int = 8000) -> int:
    server = create_server((host, port), path)
    print(f"Serving Goalkeeper at http://{host}:{server.server_port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        return 0
    finally:
        server.server_close()
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: python3 -m goalkeeper add|list|done ...", file=sys.stderr)
        return 2

    command = args[0]
    path = goals_path()
    if command == "add" and len(args) == 2:
        return add_goal(path, args[1])
    if command == "list" and len(args) == 1:
        return list_goals(path)
    if command == "done" and len(args) == 2:
        return complete_goal(path, args[1])
    if command == "serve":
        host = "127.0.0.1"
        port = 8000
        if "--host" in args:
            host_index = args.index("--host")
            if host_index + 1 >= len(args):
                print("--host requires a value", file=sys.stderr)
                return 2
            host = args[host_index + 1]
        if "--port" in args:
            port_index = args.index("--port")
            if port_index + 1 >= len(args):
                print("--port requires a value", file=sys.stderr)
                return 2
            try:
                port = int(args[port_index + 1])
            except ValueError:
                print("--port requires an integer", file=sys.stderr)
                return 2
        return serve(path, host, port)

    print("usage: python3 -m goalkeeper add|list|done|serve ...", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
