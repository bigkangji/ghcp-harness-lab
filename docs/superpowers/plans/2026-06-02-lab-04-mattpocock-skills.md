# Lab 04 Matt Pocock Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a complete Lab 04 for `mattpocock/skills` to the existing GHCP harness lab repository.

**Architecture:** Follow the existing lab structure exactly: each lab has `README.md`, `install.sh`, `prompts.md`, and `sample-app` context files. Shared documentation and tests list every supported lab explicitly, so those files must be updated with the new lab.

**Tech Stack:** Markdown documentation, Bash install scripts, Python `unittest` structure tests.

---

### Task 1: Add Lab 04 Files

**Files:**
- Create: `labs/04-mattpocock-skills/README.md`
- Create: `labs/04-mattpocock-skills/install.sh`
- Create: `labs/04-mattpocock-skills/prompts.md`
- Create: `labs/04-mattpocock-skills/sample-app/AGENTS.md`
- Create: `labs/04-mattpocock-skills/sample-app/BRIEF.md`
- Create: `labs/04-mattpocock-skills/sample-app/CONTEXT.md`
- Create: `labs/04-mattpocock-skills/sample-app/docs/adr/0001-decision-log-format.md`

- [ ] **Step 1: Write the lab README**

Use the same seven headings as the previous labs: Prereq, Install, Configure, Brief, Design, Implement, Verify & Retrospect, and Removal.

- [ ] **Step 2: Write the install script**

The script must check for `npx`, print the official command, run `npx skills@latest add mattpocock/skills`, and remind the user to run `/setup-matt-pocock-skills` in the sample app.

- [ ] **Step 3: Write the GHCP prompts**

Include prompt blocks for setup, grilling with docs, TDD implementation, diagnosis/zoom-out, and retrospective.

- [ ] **Step 4: Write sample app context**

Define the `decide` CLI brief, agent rules, starter `CONTEXT.md`, and one ADR.

### Task 2: Update Shared Repository Docs

**Files:**
- Modify: `README.md`
- Modify: `docs/comparison.md`
- Modify: `docs/sdlc-overview.md`
- Modify: `docs/ghcp-cheatsheet.md`

- [ ] **Step 1: Add Lab 04 to the root README table and directory tree**

Mention the source repo, installation command, sample app, and SDLC mapping.

- [ ] **Step 2: Extend comparison docs**

Add Matt Pocock Skills as a fourth column and describe when to choose it.

- [ ] **Step 3: Add cheatsheet notes**

Document the `npx skills@latest add mattpocock/skills` command.

### Task 3: Update Verification

**Files:**
- Modify: `tests/test_lab_structure.py`
- Modify: `scripts/verify_labs.sh`
- Modify: `scripts/check_prereqs.sh`

- [ ] **Step 1: Add the new lab to structure tests**

The test entry must require `npx skills@latest add mattpocock/skills` and key README concepts `/setup-matt-pocock-skills`, `grill-with-docs`, and `tdd`.

- [ ] **Step 2: Add required files to shell verification**

Include README, install script, prompts, and BRIEF for Lab 04.

- [ ] **Step 3: Add npx/lab guidance to prereq output**

Check for `npx` and list the Lab 04 requirement.

### Task 4: Verify

**Files:**
- Test: `tests/test_lab_structure.py`
- Test: `scripts/verify_labs.sh`

- [ ] **Step 1: Make the new install script executable**

Run: `chmod +x labs/04-mattpocock-skills/install.sh`

- [ ] **Step 2: Run tests**

Run: `make test`
Expected: all structure tests pass.

- [ ] **Step 3: Run shell verification**

Run: `make verify`
Expected: all required files are reported as OK.