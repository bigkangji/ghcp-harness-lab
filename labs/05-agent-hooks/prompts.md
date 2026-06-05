# Agent Hooks 실습 프롬프트

이 랩의 핵심은 프롬프트 규칙이 아니라 `.github/hooks/noteguard-quality.json`입니다. 아래 프롬프트는 GitHub의 Copilot cloud agent에게 작업을 맡길 때 사용하는 입력 예시입니다.

## Hook File Check

```
Before starting, inspect .github/hooks/noteguard-quality.json and summarize which
Copilot cloud agent hook triggers are configured. Confirm that sessionEnd runs
make -C labs/05-agent-hooks/sample-app verify.
```

## Cloud Agent Task

```
Update Lab 05 noteguard so `python3 -m noteguard list` prints `(no notes)` when
there are no saved notes. Add or update unittest coverage first, then implement
the minimal code. The repository has Copilot cloud agent hooks in
.github/hooks/noteguard-quality.json; use the hook output to fix any lint or
test failure.
```

## Hook Failure Repair

```
The hook run failed. Read the failing command and output, explain the root cause,
make the smallest fix, and let the configured hooks run again. Do not replace the
hook with an AGENTS.md-only instruction.
```

## Local Mirror

```
Mirror the cloud-agent hook checks locally by running:
python3 -m json.tool .github/hooks/noteguard-quality.json >/dev/null
cd labs/05-agent-hooks/sample-app && make verify
```