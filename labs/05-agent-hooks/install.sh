#!/usr/bin/env bash
# Lab 05 - Agent Hooks setup helper
#
# This lab uses the GitHub Copilot cloud agent hooks format documented at:
#   https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/use-hooks
#
# The hook configuration lives at:
#   .github/hooks/noteguard-quality.json

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HOOK_FILE="$REPO_ROOT/.github/hooks/noteguard-quality.json"

if [ ! -f "$HOOK_FILE" ]; then
  echo "Error: missing hook configuration: $HOOK_FILE"
  exit 1
fi

echo ">> Validating hook JSON: .github/hooks/noteguard-quality.json"
python3 -m json.tool "$HOOK_FILE" >/dev/null

if python3 -m ruff --version >/dev/null 2>&1; then
  echo ">> ruff found: $(python3 -m ruff --version)"
else
  echo "ruff is not installed for this Python interpreter."
  echo "Install it with one of these commands:"
  echo "  python3 -m pip install --user ruff"
  echo "  uv tool install ruff"
fi

echo
echo "Agent Hooks lab setup check complete."
echo "Next steps:"
echo "  1) Commit .github/hooks/noteguard-quality.json to the default branch"
echo "  2) Start a GitHub Copilot cloud agent session on GitHub"
echo "  3) Ask the agent to edit labs/05-agent-hooks/sample-app/noteguard.py"
echo "  4) Observe postToolUse lint and sessionEnd verify hooks"