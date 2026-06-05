# Lab 06: Copilot Goals (GHCP)

> OpenAI Codex의 `/goal` 패턴을 GitHub Copilot prompt file로 구현하고, GHCP 채팅창에서 `/goal`처럼 사용하는 실습.

원본: <https://developers.openai.com/codex/use-cases/follow-goals>

핵심: prompt file slash command → durable objective → `.goal/STATE.md` → checkpoint loop → verifiable stopping condition.
이 랩에서 말하는 goal은 Codex CLI의 native background goal이 아니라, **GHCP prompt file과 저장된 상태 파일로 재현하는 long-running work contract**입니다.

---

## 1. Prereq

```bash
# 저장소 루트에서
make prereqs
```

다음이 필요합니다.

- GitHub Copilot Chat 또는 `copilot` CLI
- VS Code에서 prompt files 지원
- `git`
- Python 3.9+ (샘플 앱 검증용)

## 2. Install

`install.sh`는 랩의 `goal.prompt.md` 템플릿을 샘플 앱의 `.github/prompts/goal.prompt.md`로 복사하고, VS Code workspace 설정에 prompt files 위치를 등록합니다.

```bash
bash labs/06-copilot-goals/install.sh
```

설치 후 샘플 앱에 다음 파일이 생깁니다.

- `sample-app/.github/prompts/goal.prompt.md` — GHCP 채팅창의 `/goal` 명령
- `sample-app/.vscode/settings.json` — `chat.promptFiles`와 `.github/prompts` 위치 설정

> VS Code가 이미 열려 있다면 window reload가 필요할 수 있습니다.

## 3. Configure

샘플 앱 폴더에서 GHCP 세션을 시작합니다.

```bash
cd labs/06-copilot-goals/sample-app
copilot
```

VS Code Copilot Chat을 쓴다면 샘플 앱 폴더를 workspace로 열고, Chat을 Agent mode로 둔 뒤 `/goal`을 입력합니다.

## 4. Brief

만들 것: **목표 추적 CLI (`goalkeeper`)**

- 목표를 `goals.md`에 추가
- 저장된 목표를 번호와 상태로 출력
- N번째 목표를 done으로 표시
- `GOALKEEPER_FILE`로 저장 파일 위치 override
- 빈 목표는 거부

자세한 사양: [`sample-app/BRIEF.md`](sample-app/BRIEF.md)

## 5. Design (`/goal` contract)

이 랩의 설계 대상은 앱 자체보다 **GHCP가 오래 걸리는 작업을 어떤 계약으로 계속 추적할지**입니다.

[`prompts.md`](prompts.md)의 **Install Check** 섹션으로 `/goal` 명령이 등록됐는지 확인합니다. 이어서 **Set Goal** 섹션을 실행하면 GHCP가 먼저 `.goal/STATE.md`를 만들고 다음 항목을 확정해야 합니다.

- Objective: 한 문장 목표
- Stopping condition: `make verify`가 통과하는 검증 가능한 완료 상태
- Non-goals: 데이터베이스, 웹 UI, 외부 런타임 의존성 제외
- Validation: `make lint`, `make test`, `make verify`
- Checkpoints: 테스트 추가, 구현, CLI 동작 확인, 최종 검증

## 6. Implement (checkpoint loop)

[`prompts.md`](prompts.md)의 **Set Goal** 프롬프트를 GHCP에 붙여넣습니다.

핵심은 한 번의 응답으로 끝내는 것이 아니라, GHCP가 아래 루프를 상태 파일에 남기면서 진행하는지 확인하는 것입니다.

```bash
make lint
make test
make verify
```

작업 중간에 `/goal`을 입력하면 현재 checkpoint, 검증 결과, 남은 일을 보고해야 합니다. `/goal pause`, `/goal resume`, `/goal clear`도 같은 prompt file 안에서 처리됩니다.

## 7. Verify & Retrospect

검증:

```bash
cd labs/06-copilot-goals/sample-app
make verify
```

회고 질문:

- `/goal <objective>`가 코딩 전에 `.goal/STATE.md`를 만들었는가?
- 목표가 하나의 durable objective와 하나의 stopping condition으로 정리됐는가?
- 각 checkpoint마다 검증 명령과 결과가 progress log에 남았는가?
- `/goal` status가 현재 checkpoint, verified, remaining, blocked를 짧게 보고했는가?
- Copilot에서 이 패턴의 한계는 무엇인가? Codex native goal처럼 완전한 background daemon은 아니라는 점을 사용자에게 설명했는가?

## 제거

샘플 앱에서 생성된 prompt command와 상태 파일을 삭제하려면 다음을 제거하세요.

```bash
rm -rf labs/06-copilot-goals/sample-app/.github/prompts
rm -rf labs/06-copilot-goals/sample-app/.goal
rm -f labs/06-copilot-goals/sample-app/.vscode/settings.json
```

전역 GHCP 설정은 변경하지 않습니다.
