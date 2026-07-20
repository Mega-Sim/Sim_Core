#!/usr/bin/env python3
"""Lightweight repository smoke check used by the simple runner UI."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def git_value(*args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=False,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        return result.stdout.strip() or "확인 불가"
    except OSError:
        return "확인 불가"


def architecture_version() -> str:
    readme = ROOT / "README.md"
    if not readme.exists():
        return "확인 불가"
    text = readme.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"현재 기준 설계는 `Architecture v(\d+)`", text)
    return f"Architecture v{match.group(1)}" if match else "확인 불가"


def executable_candidates() -> list[Path]:
    return [
        ROOT / "build" / "sim-core.exe",
        ROOT / "build" / "sim-core",
        ROOT / "build" / "sim_core_cli.exe",
        ROOT / "build" / "sim_core_cli",
        ROOT / "apps" / "sim_core_cli.py",
        ROOT / "apps" / "main.py",
    ]


def main() -> int:
    print("=== Sim_Core 최신 체크아웃 상태 ===")
    print(f"브랜치       : {git_value('branch', '--show-current')}")
    print(f"커밋         : {git_value('rev-parse', '--short', 'HEAD')}")
    print(f"설계 기준    : {architecture_version()}")

    found = [path.relative_to(ROOT) for path in executable_candidates() if path.exists()]
    if found:
        print("실행 진입점   : 발견")
        for path in found:
            print(f"  - {path}")
    else:
        print("실행 진입점   : 아직 없음")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
