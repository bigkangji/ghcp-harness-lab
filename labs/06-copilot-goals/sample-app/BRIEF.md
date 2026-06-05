# goalkeeper Brief

Build a tiny Python CLI that stores goals in a markdown file. The purpose of the lab is to practice a Copilot `/goal` command that keeps state in `.goal/STATE.md` while implementing this app.

## Requirements

- `python3 -m goalkeeper add "text"` appends a goal to `goals.md`.
- `python3 -m goalkeeper list` prints saved goals in numbered order.
- `python3 -m goalkeeper done N` marks the Nth goal as done.
- `GOALKEEPER_FILE` overrides the default goals file path for tests and scripts.
- Empty or whitespace-only goals are rejected.
- Stored goals use markdown checkboxes:
  - pending: `- [ ] goal text`
  - done: `- [x] goal text`

## Non-goals

- No database.
- No web UI.
- No goal editing or deletion.
- No third-party runtime dependency for app code.
- No native Codex or Copilot background daemon.

## 완료 정의

- `/goal` creates or updates `.goal/STATE.md` before app code changes.
- `make lint` passes.
- `make test` passes.
- `make verify` passes.
- The final GHCP response includes GOAL/STATUS/CHECKPOINT/VERIFIED/REMAINING/BLOCKED.
