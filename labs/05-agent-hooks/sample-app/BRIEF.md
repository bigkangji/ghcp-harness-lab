# noteguard Brief

Build a tiny Python CLI that stores short notes in a markdown file and uses
agent-side hook rules to keep every change verified by lint and tests.

## Requirements

- `python3 -m noteguard add "text"` appends a note to `notes.md`.
- `python3 -m noteguard list` prints saved notes in numbered order.
- `NOTEGUARD_FILE` overrides the default notes file path for tests and scripts.
- Empty or whitespace-only notes are rejected.
- Stored notes use a simple markdown list format: `- note text`.

## Non-goals

- No database.
- No note editing or deletion.
- No third-party runtime dependency for app code.
- No native git hook installation.

## 완료 정의

- `make lint` passes.
- `make test` passes.
- `make verify` passes.
- GHCP final responses report the verification commands that were run.