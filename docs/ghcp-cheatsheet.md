# GHCP Cheatsheet

이 랩을 진행할 때 자주 쓰는 GitHub Copilot CLI 명령입니다.

## 인증

```bash
gh auth status                  # GitHub 인증 상태 확인
gh auth login                   # 필요 시 로그인 (Ouroboros 랩에서 사용)
```

## 플러그인 마켓플레이스

```bash
copilot plugin marketplace add <owner>/<repo>
copilot plugin marketplace list
copilot plugin install <name>@<marketplace>
copilot plugin list
copilot plugin remove <name>
```

## 세션 진입

```bash
copilot                         # 인터랙티브 세션 시작
copilot --help                  # 옵션 확인
```

## skills.sh 설치

Matt Pocock Skills 랩은 `skills` installer를 사용합니다.

```bash
npx skills@latest add mattpocock/skills
```

설치 후 GHCP 세션에서 `/setup-matt-pocock-skills`를 실행해 문서 위치와 이슈 트래커 방식을 설정합니다.

## Copilot cloud agent hooks

Agent Hooks 랩은 GitHub Copilot cloud agent의 공식 `.github/hooks/*.json` 설정을 사용합니다.

```bash
python3 -m json.tool .github/hooks/noteguard-quality.json >/dev/null
```

로컬에서 hook command와 같은 검증을 mirror하려면 다음을 실행합니다.

```bash
cd labs/05-agent-hooks/sample-app
make lint      # python3 -m ruff check .
make test      # python3 -m unittest discover -s tests -v
make verify    # lint + test; sessionEnd hook과 같은 검증
```

cloud agent hook 파일은 repository default branch의 `.github/hooks/`에 있어야 실행됩니다.

## Prompt file slash command

Copilot Goals 랩은 VS Code/GHCP prompt file을 사용해 `/goal` 명령을 제공합니다.

```bash
bash labs/06-copilot-goals/install.sh
cd labs/06-copilot-goals/sample-app
copilot
```

GHCP 또는 VS Code Copilot Chat Agent mode에서 사용합니다.

```text
/goal
/goal Implement the goalkeeper CLI described in BRIEF.md without stopping until make verify passes.
/goal pause
/goal resume
/goal clear
```

상태와 progress log는 `.goal/STATE.md`에 기록됩니다.

## MCP 서버 확인

GHCP MCP 설정은 보통 `~/.copilot/mcp-config.json`에 위치합니다.

```bash
cat ~/.copilot/mcp-config.json 2>/dev/null || echo "MCP config 없음"
```

## 흔한 문제

| 증상 | 해결 |
| --- | --- |
| `copilot: command not found` | `npm i -g @github/copilot-cli` 또는 공식 가이드 참고 |
| `plugin install` 실패 | `gh auth login`으로 재인증 |
| MCP 서버가 보이지 않음 | GHCP 세션을 재시작 |
| `python3 -m ruff` 실패 | `python3 -m pip install --user ruff` 또는 `uv tool install ruff` |
