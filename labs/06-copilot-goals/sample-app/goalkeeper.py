"""Goalkeeper CLI skeleton for lab 06."""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: python3 -m goalkeeper add|list|done ...", file=sys.stderr)
        return 2
    print("goalkeeper is not implemented yet", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
