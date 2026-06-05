---
description: Follow one durable goal with checkpoints and a verifiable stopping condition.
agent: agent
tools: ['search/codebase', 'search', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'execute/createAndRunTask', 'execute/runTask', 'read/getTaskOutput', 'read/problems', 'changes', 'execute/testFailure', 'todo', 'web/fetch', 'search/usages']
---

# /goal — Follow a durable goal

You are running `/goal`, a Copilot prompt-file version of Codex's follow-goals workflow. The command should keep working toward **one durable objective** with a clear validation loop instead of treating the request as a one-turn task.

If the total number of checkpoints exceeds 10, pause after checkpoint 5 and ask the user to confirm continuing. This prevents unbounded autonomous execution on underspecified goals.

The user's text after `/goal` is the argument.

## Parse the argument

Before processing any argument, check whether `.goal/STATE.md` exists and note its Status field. Then apply these rules:

- Empty or `status` + `.goal/STATE.md` exists: read `.goal/STATE.md` and report status only. Do not edit code.
- `pause` + `.goal/STATE.md` exists: set status to `PAUSED`, append a handoff note to the `## Progress log` section of `.goal/STATE.md` that includes (1) the last completed checkpoint, (2) what was in progress, and (3) the exact next action needed to resume, then stop.
- `resume` + `.goal/STATE.md` exists: if Status is `DONE`, inform the user the goal is already complete and show the final `VERIFIED` line. If Status is `BLOCKED`, display the blocker and ask the user to resolve it before resuming. Only transition to `ACTIVE` if Status is `PAUSED`, then continue the next checkpoint.
- `clear` + `.goal/STATE.md` exists: ensure `.goal/archive/` exists, archive `.goal/STATE.md` to `.goal/archive/<timestamp>-STATE.md`, then report that no active goal remains. If the archive write fails, report the error and do not delete `.goal/STATE.md`.
- Anything else + `.goal/STATE.md` exists: do not overwrite it. If Status is `ACTIVE`, ask the user to run `/goal clear` or `/goal pause` before starting a new goal. For any other Status, ask the user to run `/goal clear` before starting a new goal.
- Anything else + no `.goal/STATE.md`: treat the entire argument as a new goal objective.

If a status/control command is used before `.goal/STATE.md` exists, say there is no active goal and show brief usage examples.

## Establish the contract for a new goal

Before editing code, create `.goal/STATE.md` with:

1. Objective: one durable sentence.
2. Stopping condition: one verifiable end state.
3. Non-goals / constraints.
4. Inputs to read first.
5. Validation command(s).
6. Checkpoints, each with a proving command.

If the objective is vague and no reliable stopping condition can be inferred, ask one focused clarification question instead of coding.

## Work the loop

For each checkpoint:

1. Make the minimal code change that causes the checkpoint's proving command to pass — no more, no less. Do not add functionality beyond what the proving command verifies.
2. Run the validation command(s) that prove it.
3. Update `.goal/STATE.md` with the checkpoint result and command output summary.
4. Update the visible todo list.
5. After each checkpoint's proving command passes, advance to the next checkpoint. If a proving command fails, attempt one fix and re-run. If it fails again, halt with STATUS: BLOCKED and describe the failure.

Do not claim success without running the proving command. Keep edits minimal and respect non-goals.

If a proving command exits non-zero or its output does not match the expected result, do not advance the checkpoint. Record the failure in the `## Progress log` with the exact command output, set STATUS: BLOCKED, populate `## Blocker` with the failure summary, and stop the loop.

## Stop conditions

Stop only when:

- The stopping condition is verified.
- You are blocked by: missing access, an unavoidable user decision, a validation command that cannot be executed in the current environment (e.g., missing dependency, service not running), or a proving command that does not exist. In all cases, set STATUS: BLOCKED, describe the specific cause under `## Blocker`, and stop.
- The user asked to pause.

Always end working turns with:

```text
GOAL: <one line>
STATUS: ACTIVE | PAUSED | BLOCKED | DONE
CHECKPOINT: <n>/<total> — <name>
VERIFIED: <command -> result>
REMAINING: <next checkpoint + proving command>
BLOCKED: <none | specific blocker>
```

## State template

```markdown
# Goal

**Objective:** <one durable sentence>
**Status:** ACTIVE
**Started:** <timestamp>
**Updated:** <timestamp>

## Stopping condition
<verifiable end state>

## Non-goals / constraints
- <constraint>

## Validation
- `<command>` -> expected: <result>

## Checkpoints
- [ ] 1. <name> — proven by `<command>`
- [ ] 2. <name> — proven by `<command>`

## Progress log
- <timestamp> — <checkpoint> — <what changed> — <verification result>

## Blocker
none
```

## Usage

- `/goal Implement BRIEF.md without stopping until make verify passes.`
- `/goal`
- `/goal pause`
- `/goal resume`
- `/goal clear`
