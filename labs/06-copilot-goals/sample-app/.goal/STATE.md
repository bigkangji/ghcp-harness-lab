# Goal

**Objective:** Build a simple web version of the todo app while preserving the existing CLI contract.
**Status:** DONE
**Started:** 2026-06-05T02:26:25Z
**Updated:** 2026-06-05T02:29:00Z

## Stopping condition
`make verify` passes after the app supports the CLI requirements from `BRIEF.md` and a standard-library web interface for listing, adding, and completing todo items.

## Non-goals / constraints
- Use Python standard library only for app code.
- Preserve the CLI entrypoint `python3 -m goalkeeper ...`.
- Preserve markdown checkbox storage and `GOALKEEPER_FILE` override behavior.
- Keep the web version simple: list todos, add a todo, mark a todo done.
- Do not add goal editing, deletion, databases, or third-party runtime dependencies.

## Inputs read first
- `BRIEF.md`
- `AGENTS.md`
- `tests/test_goalkeeper.py`
- `goalkeeper.py`
- `Makefile`

## Validation
- `python3 -m unittest discover -s tests -v` -> expected: all tests pass.
- `make lint` -> expected: `goalkeeper.py` compiles.
- `make verify` -> expected: lint and tests pass.

## Checkpoints
- [x] 1. CLI contract implemented — proven by `python3 -m unittest discover -s tests -v`
- [x] 2. Web todo behavior covered — proven by `python3 -m unittest discover -s tests -v`
- [x] 3. Final verification — proven by `make verify`

## Progress log
- 2026-06-05T02:26:25Z — Goal contract — Created durable state for the new web todo objective — verification pending
- 2026-06-05T02:27:10Z — CLI RED — Ran `python3 -m unittest discover -s tests -v`; 4 tests failed because `goalkeeper` is not implemented yet — expected RED result
- 2026-06-05T02:28:30Z — CLI GREEN — Implemented add/list/done markdown checkbox storage; `python3 -m unittest discover -s tests -v` passed 4 tests — checkpoint 1 complete
- 2026-06-05T02:28:40Z — Web RED — Added HTTP integration test and ran `python3 -m unittest discover -s tests -v`; 1 error because `goalkeeper.create_server` is missing — expected RED result
- 2026-06-05T02:28:50Z — Web GREEN — Implemented `create_server` and `serve`; `python3 -m unittest discover -s tests -v` passed 5 tests — checkpoint 2 complete
- 2026-06-05T02:29:00Z — Final verification — Ran `make verify`; `py_compile` passed and 5 unittest tests passed — stopping condition verified

## Blocker
none