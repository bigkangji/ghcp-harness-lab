---
description: Follow one durable goal with checkpoints and a verifiable stopping condition.
mode: agent
tools: ['codebase', 'search', 'editFiles', 'runCommands', 'runTasks', 'problems', 'changes', 'testFailure', 'todos', 'fetch', 'usages']
---

# /goal — Follow a durable goal

You are running `/goal`, a Copilot prompt-file version of Codex's follow-goals workflow. The command should keep working toward **one durable objective** with a clear validation loop instead of treating the request as a one-turn task.

The user's text after `/goal` is the argument.

## Parse the argument

- Empty or `status`: read `.goal/STATE.md` and report status only. Do not edit code.
- `pause`: set status to `PAUSED`, write a short handoff note, and stop.
- `resume`: set status to `ACTIVE`, read state, and continue the next checkpoint.
- `clear`: archive `.goal/STATE.md` to `.goal/archive/<timestamp>-STATE.md`, then report that no active goal remains.
- Anything else: treat the entire argument as a new goal objective.

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

1. Make the smallest scoped change that advances the checkpoint.
2. Run the validation command(s) that prove it.
3. Update `.goal/STATE.md` with the checkpoint result and command output summary.
4. Update the visible todo list.
5. Continue until the stopping condition is verified or you are blocked.

Do not claim success without running the proving command. Keep edits minimal and respect non-goals.

## Stop conditions

Stop only when:

- The stopping condition is verified.
- You are blocked by missing access or an unavoidable user decision.
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
