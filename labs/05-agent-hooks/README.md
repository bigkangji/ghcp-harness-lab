# Lab 05: Agent Hooks (GitHub Copilot Cloud Agent)

> GitHub Copilot cloud agent의 공식 hook 설정으로 코드 변경 뒤 lint와 test를 자동 실행하는 실습.

원본: <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/use-hooks>

핵심: `.github/hooks/NAME.json` → `sessionStart` / `postToolUse` / `sessionEnd` → shell command 실행 → lint/test 품질 게이트.

이 랩에서 말하는 hook은 prompt 규칙이나 git hook이 아니라, GitHub Copilot cloud agent가 repository default branch의 `.github/hooks/*.json` 파일을 읽어 실행하는 공식 hook입니다.

---

## 1. Prereq

```bash
# 저장소 루트에서
make prereqs
```

다음이 필요합니다.
- GitHub Copilot cloud agent를 사용할 수 있는 GitHub 환경
- repository default branch에 hook 파일을 merge할 권한
- Python 3.9+
- `ruff` (샘플 앱 lint용)
- `make`

## 2. Install

이 랩의 hook 설정은 저장소 루트의 `.github/hooks/noteguard-quality.json`에 있습니다. 공식 문서 요구사항처럼 hook 파일은 default branch에 있어야 cloud agent가 사용합니다.

`install.sh`는 로컬에서 hook JSON 문법과 `ruff` 실행 가능 여부를 확인합니다.

```bash
bash labs/05-agent-hooks/install.sh
```

`ruff`가 없다면 다음 중 하나를 실행합니다.

```bash
python3 -m pip install --user ruff
uv tool install ruff
```

## 3. Configure

hook 파일 위치:

```text
.github/hooks/noteguard-quality.json
```

이 파일은 다음 trigger를 사용합니다.

- `sessionStart`: cloud agent 세션 시작 시 `logs/copilot-hooks.log`에 시작 시간을 기록
- `postToolUse`: `labs/05-agent-hooks/sample-app/*.py` 변경이 감지되면 `make -C labs/05-agent-hooks/sample-app lint` 실행
- `sessionEnd`: 세션 종료 시 `make -C labs/05-agent-hooks/sample-app verify` 실행

중요: hook은 default branch에 merge된 뒤 cloud agent 세션에서 동작합니다. 로컬 `copilot` CLI 프롬프트만으로 hook이 자동 실행되는 것은 아닙니다.

## 4. Brief

만들 것: **노트 보호 CLI (`noteguard`)**

- `python3 -m noteguard add "text"` — `notes.md`에 노트 추가
- `python3 -m noteguard list` — 저장된 노트 출력
- `NOTEGUARD_FILE` — 테스트와 스크립트에서 파일 위치 override
- 빈 노트는 거부

자세한 사양: [`sample-app/BRIEF.md`](sample-app/BRIEF.md)

## 5. Design (Hook configuration)

이 랩의 설계 대상은 앱 자체보다 **cloud agent 실행 지점에 어떤 자동 검증을 붙일지**입니다.

hook 설정의 기본 형태는 다음과 같습니다.

```json
{
	"version": 1,
	"hooks": {
		"sessionStart": [],
		"postToolUse": [],
		"sessionEnd": []
	}
}
```

각 hook entry는 `type: "command"`, OS별 `bash`/`powershell`, 실행 위치 `cwd`, 제한 시간 `timeoutSec`를 가집니다. 이 랩은 `postToolUse`에서 Python 변경 후 lint를 돌리고, `sessionEnd`에서 전체 verify를 돌립니다.

## 6. Implement (Cloud agent hook run)

[`prompts.md`](prompts.md)의 **Cloud Agent Task** 섹션을 GitHub의 Copilot cloud agent 작업 요청에 사용합니다.

예상 흐름:

1. cloud agent가 `noteguard.py` 또는 테스트를 수정합니다.
2. `postToolUse` hook이 변경된 Python 파일을 감지하고 `make lint`를 실행합니다.
3. 세션이 끝날 때 `sessionEnd` hook이 `make verify`를 실행합니다.
4. hook 실패 시 cloud agent 작업 로그에서 실패 명령과 출력을 확인합니다.

로컬에서 같은 명령을 수동으로 확인하려면 다음을 실행합니다.

```bash
cd labs/05-agent-hooks/sample-app
make lint
make test
make verify
```

## 7. Verify & Retrospect

저장소 검증:

```bash
python3 -m json.tool .github/hooks/noteguard-quality.json >/dev/null
cd labs/05-agent-hooks/sample-app && make verify
cd ../../.. && make test && make verify
```

회고 질문:

- `.github/hooks/noteguard-quality.json`가 default branch에 있었는가?
- `postToolUse`가 Python 변경 뒤 lint를 실행했는가?
- `sessionEnd`가 `make verify`를 실행했는가?
- timeout이 너무 짧거나 너무 긴 hook은 없었는가?
- hook 실패 로그가 다음 수정 행동으로 이어질 만큼 충분히 명확했는가?

## 제거

hook을 제거하려면 default branch에서 `.github/hooks/noteguard-quality.json`을 삭제하세요. 로컬에서 `ruff`를 이 랩 때문에 설치했다면 사용한 패키지 관리자에 맞게 제거하세요.