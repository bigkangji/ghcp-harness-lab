# SDLC Overview

이 랩에서 사용하는 SDLC 7단계 정의입니다. 각 도구와 패턴은 이 단계를 다른 이름과 다른 강조점으로 다룹니다.

| # | 단계 | 목적 | 검증 가능한 산출물 |
| --- | --- | --- | --- |
| 1 | Prereq | 도구와 환경이 준비되었는가 | `make prereqs` 통과 |
| 2 | Install | 스킬/플러그인이 GHCP에서 호출 가능한가 | `copilot plugin list` 등에서 확인 |
| 3 | Configure | 프로젝트 컨텍스트(MCP, AGENTS.md, CLAUDE.md 등) 연결 | 구성 파일이 저장소에 존재 |
| 4 | Brief | 무엇을 만들지 한 문장으로 정의 | `sample-app/BRIEF.md` |
| 5 | Design | 인터뷰/브레인스토밍으로 명세 추출 | `sample-app/DESIGN.md` |
| 6 | Implement | 작은 단위로 코드와 테스트 작성 | `sample-app/src/` + 테스트 통과 |
| 7 | Verify & Retrospect | 결과 검증, 다음 반복 입력 도출 | `sample-app/RETRO.md` |

각 랩의 README는 위 단계 헤더를 동일하게 사용해 진행 상태를 추적할 수 있도록 합니다.

Lab 05 Agent Hooks는 특히 6-7단계를 강조합니다. `.github/hooks/noteguard-quality.json`에 GitHub Copilot cloud agent hook을 정의하고, `postToolUse`에서 `make lint`, `sessionEnd`에서 `make verify`를 실행하도록 합니다.

Lab 06 Copilot Goals는 5-7단계를 하나의 long-running work contract로 묶습니다. `/goal <objective>`가 `.goal/STATE.md`에 objective, stopping condition, checkpoint, validation 결과를 기록하고, `make verify` 같은 검증 가능한 종료 조건이 통과할 때까지 진행하도록 합니다.
