# BRIEF — decide

## 한 문장

팀의 작은 결정을 마크다운 파일에 기록하고, 아직 보류 중인 결정을 CLI로 추적한다.

## 사용자 시나리오

```bash
$ decide add "Use markdown for the decision log" --why "easy to review in git"
Added #1: Use markdown for the decision log

$ decide list
- [ ] 1. Use markdown for the decision log — easy to review in git

$ decide accept 1
Accepted: Use markdown for the decision log

$ decide list
No pending decisions.
```

## 요구사항

- 파일 경로: 환경변수 `DECIDE_FILE` 또는 기본값 `./decisions.md`
- `add "텍스트" --why "이유"`는 보류 중인 결정을 파일 끝에 추가
- `list`는 accepted가 아닌 결정을 1부터 다시 매겨 출력
- `accept <N>`은 현재 보류 중인 결정 중 N번째를 accepted로 표시
- 결정 줄은 사람이 읽을 수 있는 마크다운이어야 함
- 잘못된 N, 누락된 `--why`, 알 수 없는 명령은 stderr 메시지와 종료코드 1

## 비목표

- 여러 사용자 동시 편집 잠금
- 원격 동기화
- 태그, 소유자, 마감일
- TUI 또는 웹 UI

## 구현 제약

- Python 3.10+ 표준 라이브러리만 사용
- 단일 모듈 `decide.py` + 진입점 `python3 -m decide ...`
- 테스트는 `tests/test_decide.py`에 작성하고 `python3 -m unittest discover -s tests -v`로 실행
- `/grill-with-docs`가 확정한 용어를 코드, 테스트, 문서에서 동일하게 사용

## 완료 정의

- 위 사용자 시나리오가 자동 테스트로 통과
- add/list/accept와 오류 경로 테스트 존재
- `CONTEXT.md`, `docs/adr/`, `DESIGN.md`, `RETRO.md`가 모두 채워짐
- `/zoom-out` 점검 결과가 `RETRO.md`에 반영됨