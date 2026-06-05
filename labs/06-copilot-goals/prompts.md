# Copilot Goals 실습 프롬프트

GHCP 세션(`copilot`) 또는 VS Code Copilot Chat Agent mode에서 아래 블록을 차례대로 붙여 넣습니다.
이 랩은 Codex native `/goal`을 그대로 설치하는 것이 아니라, GHCP prompt file로 같은 작업 계약을 재현합니다.

## Install Check

```
/goal
```

기대 결과:

- 아직 `.goal/STATE.md`가 없다면 active goal이 없다고 말합니다.
- 사용법 예시로 `/goal <objective>`, `/goal pause`, `/goal resume`, `/goal clear`를 보여줍니다.

## Set Goal

```
/goal Implement the goalkeeper CLI described in BRIEF.md without stopping until `make verify` passes. Read AGENTS.md, BRIEF.md, and tests first. Keep app code on the Python standard library only. Work in checkpoints and update .goal/STATE.md after each verification command.
```

GHCP가 해야 할 일:

- `.goal/STATE.md`를 먼저 생성
- objective, stopping condition, non-goals, validation, checkpoints 기록
- todo/checkpoint를 만들고 하나씩 진행
- 테스트와 구현을 갱신
- `make lint`, `make test`, `make verify` 실행
- 최종 응답에 GOAL/STATUS/CHECKPOINT/VERIFIED/REMAINING/BLOCKED 블록 포함

## Status

작업 중간이나 완료 후 현재 상태만 확인합니다.

```
/goal
```

기대 결과:

- 코드 변경 없이 `.goal/STATE.md`만 읽습니다.
- 현재 checkpoint, 마지막 검증 결과, 남은 일, blocked 여부를 짧게 보고합니다.

## Pause / Resume

```
/goal pause
```

```
/goal resume
```

기대 결과:

- pause는 `.goal/STATE.md`의 status를 `PAUSED`로 바꾸고 멈춥니다.
- resume은 status를 `ACTIVE`로 바꾸고 다음 checkpoint부터 이어갑니다.

## Clear

```
/goal clear
```

기대 결과:

- 기존 `.goal/STATE.md`를 `.goal/archive/<timestamp>-STATE.md`로 보관합니다.
- active goal이 없다고 확인합니다.

## Tighten a vague goal

아래처럼 일부러 나쁜 목표를 줘 봅니다.

```
/goal Make the project better.
```

기대 결과:

- GHCP가 바로 코딩하지 않습니다.
- objective와 stopping condition이 모호하다고 말하고, 검증 가능한 목표로 좁히는 질문을 합니다.
