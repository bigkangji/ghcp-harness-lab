# Matt Pocock Skills 실습 프롬프트

GHCP 세션에서 아래 블록을 차례대로 붙여 넣습니다. 설치 중 선택한 에이전트 위치에 따라 슬래시 명령이 직접 동작하지 않으면, 해당 스킬의 `SKILL.md`를 먼저 읽고 같은 역할로 수행하라고 지시하세요.

## Setup

```
Run /setup-matt-pocock-skills for this repository.

Use local files as the issue tracker for this lab. Use CONTEXT.md as the shared
language document and docs/adr/ as the ADR directory. Keep generated planning
docs in this sample-app folder unless a skill requires another path.
```

## Grill With Docs

```
Use /grill-with-docs on BRIEF.md before writing code.

Challenge the terms decision, pending, accepted, and rationale. Update
CONTEXT.md and docs/adr/0001-decision-log-format.md with the final vocabulary
and decisions. Then write DESIGN.md with the accepted scope, non-goals, data
format, error handling, and test strategy.
```

## TDD Implementation

```
Use /tdd to implement DESIGN.md one vertical slice at a time.

Write tests in tests/test_decide.py first, verify they fail, then implement the
minimum in decide.py. Use only the Python standard library. After each slice,
run `python3 -m unittest discover -s tests -v`.
```

## Diagnose

```
Use /diagnose on any failing behavior from the test suite or manual CLI runs.

Follow reproduce -> minimise -> hypothesise -> instrument -> fix -> regression
test. Record the final root cause and regression test in RETRO.md.
```

## Zoom Out

```
Use /zoom-out on decide.py and the docs.

Explain how the code, CONTEXT.md, and ADRs fit together. Identify any naming or
module boundary mismatch, fix obvious ones, and leave the rest as next-iteration
notes in RETRO.md.
```

## Retrospective

```
Write RETRO.md. Include what shipped, which Matt Pocock skill changed the work
most, which feedback loop caught the most useful issue, and what should happen
in the next iteration.
```