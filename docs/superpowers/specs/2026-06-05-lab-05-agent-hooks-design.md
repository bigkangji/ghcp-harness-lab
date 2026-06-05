# Lab 05 Agent Hooks Design

## Goal

Add a fifth lab focused on GitHub Copilot cloud agent hooks: using `.github/hooks/*.json` so the cloud agent runs lint and tests at defined execution triggers.

The lab should teach the official hooks mechanism from GitHub Docs. Learners should leave with a reusable `.github/hooks/noteguard-quality.json` example and a small Python sample app that demonstrates lint/test feedback loops.

## Recommended Approach

Use the GitHub Copilot cloud agent hook mechanism rather than prompt-only instructions or git hooks.

1. Define `.github/hooks/noteguard-quality.json` with `version: 1`.
2. Use `sessionStart` to log session start, `postToolUse` to run lint after Python changes, and `sessionEnd` to run full verification.
3. Provide a Python sample app with real tests and lint configuration.
4. Use `ruff` for lint because it is fast, common, and easy to run through `python3 -m ruff` after installation.
5. Use `unittest` for tests to keep the sample app independent from extra test framework dependencies.
6. Use `prompts.md` only as example cloud-agent task text; the enforcement comes from `.github/hooks/*.json`.

This is the best fit because the user asked for the documented Copilot hook workflow. Lab 05 extends the comparison by showing native cloud-agent hook triggers rather than simulated hook behavior.

## Sample App

The sample app is `noteguard`, a small Python CLI for appending and listing short notes in a markdown file.

- `noteguard add "text"` appends a note to `notes.md`.
- `noteguard list` prints saved notes in order.
- `NOTEGUARD_FILE` can override the default file path for tests.
- Notes must reject empty input.
- Data lives in a simple markdown checklist/list format.

The repository should include starter code and tests for this lab because the point is to exercise hooks against concrete lint and test commands, not only to generate an app from scratch.

## Hook Configuration

`.github/hooks/noteguard-quality.json` should define the operational hook contract:

- `sessionStart`: append a session marker to `logs/copilot-hooks.log`.
- `postToolUse`: if changed files include `labs/05-agent-hooks/sample-app/*.py`, run `make -C labs/05-agent-hooks/sample-app lint`.
- `sessionEnd`: run `make -C labs/05-agent-hooks/sample-app verify`.
- Include both `bash` and `powershell` keys to match the GitHub Docs recommendation.

The lab should be clear that hooks must be present on the repository default branch to be used by Copilot cloud agent.

## Files

- Add `labs/05-agent-hooks/README.md` for the full lab guide.
- Add `.github/hooks/noteguard-quality.json` with the official hook configuration.
- Add `labs/05-agent-hooks/install.sh` to validate hook JSON and check for `ruff`.
- Add `labs/05-agent-hooks/prompts.md` with cloud-agent task examples and local mirror commands.
- Add `labs/05-agent-hooks/sample-app/AGENTS.md` pointing to the real hook configuration.
- Add `labs/05-agent-hooks/sample-app/BRIEF.md` with the `noteguard` requirements and completion definition.
- Add `labs/05-agent-hooks/sample-app/noteguard.py` as starter implementation.
- Add `labs/05-agent-hooks/sample-app/tests/test_noteguard.py` as real test coverage.
- Add `labs/05-agent-hooks/sample-app/pyproject.toml` for `ruff` configuration.
- Add `labs/05-agent-hooks/sample-app/Makefile` with `lint`, `test`, and `verify` targets.
- Update root README, shared docs, verification script, and structure tests to know about Lab 05.

## Testing

- `make test` at the repository root should include the new lab and check its required files, install script content, and README keywords.
- `make verify` should include the new lab's required files.
- `python3 -m json.tool .github/hooks/noteguard-quality.json >/dev/null` should validate hook JSON.
- `cd labs/05-agent-hooks/sample-app && make verify` should run lint and tests for the sample app.

## Scope

This lab does not configure git hooks and does not rely on prompt-only enforcement. It demonstrates official Copilot cloud agent hooks plus deterministic local commands. The sample app stays intentionally small so the educational focus remains on verification discipline: lint, test, repair, rerun, and report.