# Lab 05 Agent Hooks Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Lab 05, a GitHub Copilot cloud agent hook lab that teaches lint/test verification hooks through a Python sample app.

**Architecture:** The lab mirrors the existing `labs/0N-*` structure and adds a concrete `noteguard` sample app. Hook behavior is expressed through `.github/hooks/noteguard-quality.json`, while `Makefile`, `ruff`, and `unittest` provide deterministic verification commands.

**Tech Stack:** Markdown lab docs, Bash install script, Python 3 standard library, `unittest`, `ruff`, Make.

---

## File Structure

- `tests/test_lab_structure.py`: add Lab 05 expectations so repository tests fail before files exist.
- `scripts/verify_labs.sh`: include Lab 05 required files in shell verification.
- `.github/hooks/noteguard-quality.json`: official Copilot cloud agent hook configuration.
- `labs/05-agent-hooks/README.md`: learner-facing guide using the existing 7-stage lab flow.
- `labs/05-agent-hooks/install.sh`: executable helper that checks `ruff` availability and prints install guidance.
- `labs/05-agent-hooks/prompts.md`: example cloud-agent task prompts and local mirror commands.
- `labs/05-agent-hooks/sample-app/AGENTS.md`: points agents to the real hook configuration.
- `labs/05-agent-hooks/sample-app/BRIEF.md`: `noteguard` requirements and completion definition.
- `labs/05-agent-hooks/sample-app/Makefile`: `lint`, `test`, and `verify` targets.
- `labs/05-agent-hooks/sample-app/pyproject.toml`: `ruff` configuration.
- `labs/05-agent-hooks/sample-app/tests/test_noteguard.py`: executable sample-app tests.
- `labs/05-agent-hooks/sample-app/noteguard.py`: minimal CLI implementation that passes tests.
- `README.md`, `docs/comparison.md`, `docs/sdlc-overview.md`, `docs/ghcp-cheatsheet.md`: mention Lab 05 and its verification-hook role.

## Task 1: Red Test For Lab 05 Structure

**Files:**
- Modify: `tests/test_lab_structure.py`

- [ ] **Step 1: Add Lab 05 expectations**

Add `05-agent-hooks` to `LABS` with `tool_name` set to `Agent Hooks`, `install_must_contain` fragments `.github/hooks/noteguard-quality.json` and `python3 -m json.tool`, and README keywords `.github/hooks/noteguard-quality.json`, `sessionEnd`, `postToolUse`, `make lint`, `make verify`.

- [ ] **Step 2: Run repository tests to verify failure**

Run: `python3 -m unittest tests.test_lab_structure -v`
Expected: FAIL because `labs/05-agent-hooks/*` files do not exist yet.

## Task 2: Red Test For Sample App

**Files:**
- Create: `labs/05-agent-hooks/sample-app/tests/test_noteguard.py`

- [ ] **Step 1: Write sample app tests**

Create tests for adding a note, listing notes, rejecting empty input, and honoring `NOTEGUARD_FILE`.

- [ ] **Step 2: Run sample tests to verify failure**

Run: `cd labs/05-agent-hooks/sample-app && python3 -m unittest discover -s tests -v`
Expected: FAIL because `noteguard.py` does not exist yet.

## Task 3: Implement Sample App Verification Surface

**Files:**
- Create: `labs/05-agent-hooks/sample-app/noteguard.py`
- Create: `labs/05-agent-hooks/sample-app/Makefile`
- Create: `labs/05-agent-hooks/sample-app/pyproject.toml`

- [ ] **Step 1: Write minimal implementation**

Implement `add_note`, `list_notes`, `resolve_notes_file`, and a small `main` CLI using only the Python standard library.

- [ ] **Step 2: Add lint/test commands**

Add Make targets:

```makefile
lint:
	python3 -m ruff check .

test:
	python3 -m unittest discover -s tests -v

verify: lint test
```

- [ ] **Step 3: Run sample tests**

Run: `cd labs/05-agent-hooks/sample-app && python3 -m unittest discover -s tests -v`
Expected: PASS.

## Task 4: Add Lab 05 Guide Files

**Files:**
- Create: `labs/05-agent-hooks/README.md`
- Create: `labs/05-agent-hooks/install.sh`
- Create: `labs/05-agent-hooks/prompts.md`
- Create: `labs/05-agent-hooks/sample-app/AGENTS.md`
- Create: `labs/05-agent-hooks/sample-app/BRIEF.md`

- [ ] **Step 1: Add learner guide and prompts**

Write the 7-stage lab guide, install helper, and cloud-agent prompts that exercise official `.github/hooks` triggers.

- [ ] **Step 2: Mark install script executable**

Run: `chmod +x labs/05-agent-hooks/install.sh`

## Task 5: Update Shared Documentation And Verifiers

**Files:**
- Modify: `README.md`
- Modify: `docs/comparison.md`
- Modify: `docs/sdlc-overview.md`
- Modify: `docs/ghcp-cheatsheet.md`
- Modify: `scripts/verify_labs.sh`

- [ ] **Step 1: Add Lab 05 to shared docs**

Update root and shared docs so Lab 05 appears alongside the existing labs.

- [ ] **Step 2: Add Lab 05 to shell verifier**

Append Lab 05 required files to `scripts/verify_labs.sh`.

## Task 6: Full Verification

**Files:**
- All changed files

- [ ] **Step 1: Run sample verification**

Run: `cd labs/05-agent-hooks/sample-app && make verify`
Expected: `ruff` exits 0 and all `unittest` tests pass.

- [ ] **Step 2: Run repository verification**

Run: `make test && make verify`
Expected: repository structure tests and shell verifier pass.

- [ ] **Step 3: Inspect status**

Run: `git --no-pager status --short`
Expected: only intentional Lab 05, docs, test, and verifier changes plus pre-existing unrelated generated files.