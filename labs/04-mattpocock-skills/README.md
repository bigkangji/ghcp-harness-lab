# Lab 04: Matt Pocock Skills (GHCP)

> Matt Pocock의 작고 조합 가능한 엔지니어링 스킬을 GHCP에 설치하고, 도메인 문서화와 TDD 루프로 작은 CLI를 만들어보는 실습.

원본: <https://github.com/mattpocock/skills>

핵심: `/setup-matt-pocock-skills` → `/grill-with-docs` → `/tdd` → `/diagnose` → `/zoom-out`. **큰 프레임워크가 아니라, 실제 엔지니어링 습관을 작은 스킬로 끼워 넣는 방식**.

---

## 1. Prereq

- `node` / `npm` / `npx`
- `copilot` CLI
- `git`
- Python 3.10+ (샘플 앱 구현용)

```bash
make prereqs
```

## 2. Install

`install.sh`는 Matt Pocock Skills README의 quickstart 명령을 실행합니다.

```bash
bash labs/04-mattpocock-skills/install.sh
```

공식 quickstart의 핵심 명령:

```bash
npx skills@latest add mattpocock/skills
```

설치 중 어떤 에이전트에 설치할지 묻는 선택지가 나오면 GHCP/Copilot에 해당하는 항목을 고르고, `/setup-matt-pocock-skills`를 포함해 설치하세요.

> 이 명령은 사용자 홈 디렉터리의 에이전트 스킬 설정을 바꿀 수 있습니다. 실행 전 스크립트 내용을 먼저 확인하세요.

## 3. Configure

설치 후 샘플 앱 폴더에서 GHCP를 시작합니다.

```bash
cd labs/04-mattpocock-skills/sample-app
copilot
```

첫 세션에서는 [`prompts.md`](prompts.md)의 **Setup** 프롬프트를 실행합니다. `/setup-matt-pocock-skills`가 다음을 묻습니다.

- 이슈 트래커: GitHub, Linear, local files 중 무엇을 쓸지
- triage 라벨 이름
- 문서와 ADR을 어디에 저장할지

이 랩에서는 local files를 선택하고 문서 위치는 현재 샘플 앱의 `CONTEXT.md`, `docs/adr/`를 사용합니다.

## 4. Brief

만들 것: **결정 기록 CLI (`decide`)**

- 결정 후보를 `decisions.md`에 추가
- 아직 보류 중인 결정을 번호로 출력
- N번째 보류 결정을 accepted로 바꿈
- 왜 이 결정을 하는지 `--why`로 기록

자세한 사양: [`sample-app/BRIEF.md`](sample-app/BRIEF.md)

## 5. Design (`/grill-with-docs`)

[`prompts.md`](prompts.md)의 **Grill With Docs** 섹션을 붙여넣습니다.

이 단계의 목적은 구현 전에 용어를 정리하는 것입니다.

- `decision`, `pending`, `accepted`, `rationale`이 무엇을 뜻하는지 확정
- `CONTEXT.md`에 공유 언어 추가
- `docs/adr/`에 결정 포맷 ADR 업데이트
- `DESIGN.md`에 범위와 비목표 작성

## 6. Implement (`/tdd`)

[`prompts.md`](prompts.md)의 **TDD Implementation** 섹션을 실행합니다.

샘플 앱 구현 제약:

- Python 표준 라이브러리만 사용
- 단일 모듈 `decide.py`
- 진입점 `python3 -m decide ...`
- 테스트는 `tests/test_decide.py`

핵심은 기능을 한 번에 만들지 않고, 각 동작을 RED → GREEN → REFACTOR로 통과시키는 것입니다.

## 7. Verify & Retrospect (`/diagnose` + `/zoom-out`)

검증:

```bash
cd labs/04-mattpocock-skills/sample-app
python3 -m unittest discover -s tests -v
```

문제가 생기면 `/diagnose`로 재현 → 최소화 → 가설 → 계측 → 수정 → 회귀 테스트 루프를 돌립니다.

마지막으로 `/zoom-out`을 사용해 `decide.py`, `CONTEXT.md`, ADR이 같은 도메인 언어를 쓰는지 점검하고, 결과를 `RETRO.md`에 기록합니다.

## 제거

Matt Pocock Skills는 `skills` installer가 선택한 에이전트별 위치에 파일을 설치합니다. 제거하려면 설치 시 출력된 경로 또는 해당 에이전트의 skills 디렉터리에서 `mattpocock/skills` 관련 파일을 삭제하세요.