#!/usr/bin/env bash
# Lab 04 - Matt Pocock Skills GHCP 설치 스크립트
#
# 공식 quickstart(README.md 참조):
#   npx skills@latest add mattpocock/skills
#
# 실행 중 어떤 에이전트에 설치할지 묻는 대화형 선택지가 나올 수 있습니다.
# GHCP/Copilot에 해당하는 항목과 /setup-matt-pocock-skills를 선택하세요.

set -euo pipefail

if ! command -v npx >/dev/null 2>&1; then
  echo "Error: npx가 필요합니다. Node.js/npm을 먼저 설치하세요."
  exit 1
fi

echo ">> npx skills@latest add mattpocock/skills"
npx skills@latest add mattpocock/skills

echo
echo "Matt Pocock Skills 설치 흐름 완료."
echo "다음 단계:"
echo "  1) cd labs/04-mattpocock-skills/sample-app && copilot"
echo "  2) GHCP 세션에서 /setup-matt-pocock-skills 실행"
echo "  3) prompts.md의 Grill With Docs부터 진행"