# 네 도구 비교

| 항목 | Superpowers | gstack | Ouroboros | Matt Pocock Skills |
| --- | --- | --- | --- | --- |
| 만든 사람 | Jesse Vincent (obra) | Garry Tan (YC) | Q00 | Matt Pocock |
| 핵심 비유 | "스킬 라이브러리" | "전문가 23명 팀" | "Agent OS" | "실전 엔지니어링 습관 묶음" |
| 워크플로우 형태 | 자동 트리거 스킬 | 슬래시 커맨드 | `ooo` 명령 + Seed/Ledger | 작은 스킬을 필요한 순간 조합 |
| 강점 | TDD 강제, 서브에이전트 검토 | 역할별 깊은 리뷰, /qa 브라우저 테스트 | 명세 불변성, replay 가능 | 도메인 언어, ADR, TDD, 진단 루프 |
| GHCP 설치 방식 | 공식 plugin marketplace | git clone (수동 통합) | `ouroboros setup --runtime copilot` | `npx skills@latest add mattpocock/skills` |
| 산출물 위치 | 스킬이 작업 디렉터리 안에 직접 기록 | `.claude/`, `CLAUDE.md` | Seed/Ledger 파일 | `CONTEXT.md`, `docs/adr/`, 이슈/PRD 문서 |
| 적합한 작업 | 신규 기능 TDD 구현 | 제품 방향 재정의 + 출시 | 모호한 아이디어 명세화 | 기존 코드베이스의 언어 정리와 안전한 변경 |

## 언제 무엇을 쓸까

- **요구사항이 흐릿하다** → Ouroboros `ooo interview` 또는 gstack `/office-hours`
- **TDD로 안전하게 구현하고 싶다** → Superpowers `test-driven-development`
- **출시 직전 종합 검토가 필요하다** → gstack `/review` + `/cso` + `/qa`
- **여러 LLM에서 같은 결과를 재현하고 싶다** → Ouroboros Seed + Ledger
- **코드와 문서의 도메인 언어를 맞추고 싶다** → Matt Pocock `/grill-with-docs` + `/zoom-out`

## 함께 쓸 수 있는가

가능합니다. 한 저장소에서 다음과 같이 조합하는 것이 자연스럽습니다.

1. Ouroboros로 명세를 잠그고 (Seed 생성)
2. Matt Pocock `/grill-with-docs`로 공유 언어와 ADR을 정리하고
3. Superpowers 또는 Matt Pocock `/tdd`로 구현한 뒤
4. gstack `/review`, `/cso`, `/qa`로 출시 직전 검토를 수행
