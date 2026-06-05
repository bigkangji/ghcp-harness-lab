# Agent context for the Agent Hooks sample app

This is lab 05 (Agent Hooks). The lab README is at `../README.md`.

## Hook configuration

The real hook configuration for this lab lives at
`../../../.github/hooks/noteguard-quality.json`.

GitHub Copilot cloud agent reads hook configuration from `.github/hooks/*.json`
on the repository default branch. The lab hook uses:

- `sessionStart` to append a session marker to `logs/copilot-hooks.log`.
- `postToolUse` to run `make -C labs/05-agent-hooks/sample-app lint` when Python
  files in this sample app have changed.
- `sessionEnd` to run `make -C labs/05-agent-hooks/sample-app verify`.

Do not replace these hooks with prompt-only instructions. The point of this lab
is to exercise the official GitHub Copilot cloud agent hooks mechanism.

## Implementation rules

- Python standard library only for app code.
- The lint tool is `ruff`; run it through `python3 -m ruff check .`.
- Tests use `unittest`; run them with `python3 -m unittest discover -s tests -v`.
- Keep behavior small and covered by tests before claiming the task is complete.