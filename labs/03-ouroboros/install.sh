#!/usr/bin/env bash
# Lab 03 - Ouroboros GHCP runtime 설치 스크립트
#
# 공식 절차(README.md 참조):
#   1) pipx install --python <python3.12> 'ouroboros-ai[mcp]'
#      (또는 uv tool install --python <python3.12>)
#   2) ouroboros setup --runtime copilot
#   3) 버전 확인
#
# 사전: gh auth login (live model discovery에 사용)

set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "Error: gh CLI가 필요합니다."
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Error: gh 인증되지 않음. 'gh auth login' 먼저 실행하세요."
  exit 1
fi

PYTHON_BIN=""
PY_VER=""

for candidate in "${PYTHON:-}" python3.12 python3 python; do
  if [ -z "$candidate" ]; then
    continue
  fi

  if ! command -v "$candidate" >/dev/null 2>&1; then
    continue
  fi

  candidate_path=$(command -v "$candidate")
  if "$candidate_path" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)' >/dev/null 2>&1; then
    PYTHON_BIN="$candidate_path"
    PY_VER=$("$PYTHON_BIN" -c 'import sys; print("%d.%d.%d" % sys.version_info[:3])')
    break
  fi
done

if [ -z "$PYTHON_BIN" ] && command -v uv >/dev/null 2>&1; then
  echo ">> Python 3.12 실행 파일을 찾지 못했습니다. uv로 Python 3.12를 준비합니다."
  uv python install 3.12
  PYTHON_BIN=$(uv python find 3.12)
  PY_VER=$("$PYTHON_BIN" -c 'import sys; print("%d.%d.%d" % sys.version_info[:3])')
fi

if [ -z "$PYTHON_BIN" ]; then
  echo "Error: Python >= 3.12 가 필요합니다. python3.12를 설치하거나 uv를 설치하세요."
  echo "  brew install python@3.12  # 또는"
  echo "  brew install uv"
  exit 1
fi

echo ">> Using Python $PY_VER: $PYTHON_BIN"

if command -v pipx >/dev/null 2>&1; then
  echo ">> pipx install --python '$PYTHON_BIN' 'ouroboros-ai[mcp]'"
  pipx install --python "$PYTHON_BIN" 'ouroboros-ai[mcp]'
elif command -v uv >/dev/null 2>&1; then
  echo ">> uv tool install --python '$PYTHON_BIN' 'ouroboros-ai[mcp]'"
  uv tool install --python "$PYTHON_BIN" 'ouroboros-ai[mcp]'
else
  echo "Error: pipx 또는 uv 중 하나가 필요합니다."
  echo "  brew install pipx  # 또는"
  echo "  brew install uv"
  exit 1
fi

echo ">> ouroboros setup --runtime copilot"
ouroboros setup --runtime copilot

echo ">> ouroboros --version"
ouroboros --version

echo
echo "MCP 등록 확인:"
if [ -f "$HOME/.copilot/mcp-config.json" ]; then
  "$PYTHON_BIN" -m json.tool < "$HOME/.copilot/mcp-config.json" | head -n 20
else
  echo "  ~/.copilot/mcp-config.json 가 아직 없습니다. GHCP를 한 번 실행해 생성될 수 있습니다."
fi

echo
echo "Ouroboros 설치 완료. GHCP 세션을 재시작한 뒤 샘플 앱 폴더에서 시작하세요:"
echo "  cd labs/03-ouroboros/sample-app && copilot"
