# Agent context for the Matt Pocock Skills sample app

This is lab 04 (Matt Pocock Skills). The lab README is at `../README.md`.

## Matt Pocock Skills rules

- Run `/setup-matt-pocock-skills` before using the other skills in this lab.
- Use `/grill-with-docs` before implementation. It should update `CONTEXT.md`,
  `docs/adr/`, and `DESIGN.md`.
- Use `/tdd` for implementation. Do not write production code before the failing
  test for the current behavior exists.
- Use `/diagnose` for failures instead of jumping straight to fixes.
- Use `/zoom-out` before the retrospective to check whether the code and docs
  use the same domain language.

## Implementation rules

- Python 3.10+ standard library only.
- Single module `decide.py`. Entry point: `python3 -m decide`.
- Data file: `DECIDE_FILE` environment variable or `./decisions.md`.
- Tests live under `tests/`. Run with `python3 -m unittest discover -s tests -v`.
- Save design output to `DESIGN.md` and retrospective output to `RETRO.md`.