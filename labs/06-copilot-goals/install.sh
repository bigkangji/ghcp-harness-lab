#!/usr/bin/env bash
# Lab 06 - Copilot Goals setup helper
#
# This lab installs a GHCP prompt-file slash command into the sample app:
#   sample-app/.github/prompts/goal.prompt.md
# It also enables VS Code prompt files for the sample workspace via
#   "chat.promptFiles": true
#   "chat.promptFilesLocations": { ".github/prompts": true }

set -euo pipefail

LAB_DIR="$(cd "$(dirname "$0")" && pwd)"
APP_DIR="$LAB_DIR/sample-app"
PROMPT_DIR="$APP_DIR/.github/prompts"
VSCODE_DIR="$APP_DIR/.vscode"

mkdir -p "$PROMPT_DIR" "$VSCODE_DIR"
cp "$LAB_DIR/goal.prompt.md" "$PROMPT_DIR/goal.prompt.md"

cat > "$VSCODE_DIR/settings.json" <<'JSON'
{
  "chat.promptFiles": true,
  "chat.promptFilesLocations": {
    ".github/prompts": true
  }
}
JSON

echo ">> Installed /goal prompt file: $PROMPT_DIR/goal.prompt.md"
echo ">> Enabled VS Code prompt files in: $VSCODE_DIR/settings.json"
echo
echo "Copilot Goals lab setup complete."
echo "Next steps:"
echo "  1) cd labs/06-copilot-goals/sample-app && copilot"
echo "  2) In VS Code Copilot Chat Agent mode, type /goal"
echo "  3) Use prompts.md to practice the goal checkpoint loop"
