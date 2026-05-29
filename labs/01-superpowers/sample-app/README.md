# mdtodo

Small Python CLI for managing markdown checkbox todos.

## Usage

```bash
uv run python -m mdtodo add "랩 02 진행"
uv run python -m mdtodo list
uv run python -m mdtodo done 2
```

By default, `mdtodo` reads and writes `./tasks.md`.
Set `MDTODO_FILE` to use another file:

```bash
MDTODO_FILE=/tmp/tasks.md uv run python -m mdtodo list
```

Todo lines use markdown checkbox syntax:

```markdown
- [ ] incomplete task
- [x] completed task
```

`list` shows only incomplete items and renumbers them from 1.
