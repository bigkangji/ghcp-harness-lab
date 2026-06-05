# Agent context for the Copilot Goals sample app

This is lab 06 (Copilot Goals). The lab README is at `../README.md`.

## Goal contract

When the user invokes `/goal`, treat `.goal/STATE.md` as the durable state for the run.

- Read `BRIEF.md`, this file, and existing tests before editing.
- Create or update `.goal/STATE.md` before changing app code for a new goal.
- Keep one durable objective and one verifiable stopping condition.
- Work in checkpoints and update the progress log after each validation command.
- Stop only when the stopping condition is verified, the user pauses, or a real blocker requires input.

## Implementation rules

- Python standard library only for app code.
- The CLI entrypoint is `python3 -m goalkeeper ...`.
- Tests use `unittest`; run them with `python3 -m unittest discover -s tests -v`.
- `make lint` uses `python3 -m py_compile goalkeeper.py`.
- Before claiming completion, run `make verify` and report the result.
