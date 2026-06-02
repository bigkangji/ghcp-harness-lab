# Lab 04 Matt Pocock Skills Design

## Goal

Add a fourth GHCP lab for <https://github.com/mattpocock/skills>. The lab should match the existing repository pattern: install a real external skill framework, configure a sample app context, run a design/implementation/verification loop, and compare the framework against the previous labs.

## Recommended Approach

Use the representative engineering loop from Matt Pocock's skills rather than a broad catalog tour:

1. Install with `npx skills@latest add mattpocock/skills`.
2. Run `/setup-matt-pocock-skills` to configure issue tracker labels and docs locations.
3. Use `/grill-with-docs` to sharpen terminology and write domain docs.
4. Use `/tdd` to implement a tiny CLI with red-green-refactor.
5. Use `/diagnose` and `/zoom-out` as verification/reflection tools.

This is the best fit because the existing labs are SDLC-oriented. A catalog lab would show more commands but teach less about when the framework changes engineering behavior.

## Sample App

The sample app is `decide`, a small Python CLI for logging lightweight decisions. It is intentionally tiny but domain-rich enough for `CONTEXT.md` and ADRs:

- `decide add "text" --why "reason"` appends a pending decision.
- `decide list` shows pending decisions.
- `decide accept <N>` marks the Nth pending decision as accepted.
- Data lives in `DECIDE_FILE` or `./decisions.md`.

## Files

- Add `labs/04-mattpocock-skills/README.md` for the full lab guide.
- Add `labs/04-mattpocock-skills/install.sh` for the official installer command.
- Add `labs/04-mattpocock-skills/prompts.md` with copy/paste GHCP prompts.
- Add `labs/04-mattpocock-skills/sample-app/AGENTS.md` and `BRIEF.md`.
- Add a small starter `CONTEXT.md` and ADR folder in the sample app so `/grill-with-docs` has concrete documentation targets.
- Update root README, shared docs, verification script, and structure tests to know about Lab 04.

## Testing

- `make test` should include the new lab and check its install command/key concepts.
- `make verify` should include the new lab's required files.

## Scope

No implementation code for `decide` is added in this repository update. As with labs 02 and 03, the sample app code is produced by the learner during the lab.