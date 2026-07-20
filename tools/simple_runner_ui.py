#!/usr/bin/env python3
"""Sim_Core latest checkout runner UI.

A dependency-free Tkinter utility that lets a developer run the current checkout
and inspect stdout/stderr without opening a terminal window.
"""

from __future__ import annotations

import os
import queue
import subprocess
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, scrolledtext, ttk


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_capture(command: list[str]) -> str:
    try:
        result = subprocess.run(
            command,
            cwd=REPO_ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return f"명령 실행 실패: {exc}"
    return result.stdout.strip()


def current_commit() -> str:
    value = run_capture(["git", "rev-parse", "--short", "HEAD"])
    return value or "확인 불가"


def current_branch() -> str:
    value = run_capture(["git", "branch", "--show-current"])
    return value or "확인 불가"


def python_command(path: str) -> str:
    return f'"{sys.executable}" {path}'


def detect_command() -> str:
    candidates = [
        (REPO_ROOT / "build" / "sim-core.exe", '"build\\sim-core.exe" --help'),
        (REPO_ROOT / "build" / "sim-core", './build/sim-core --help'),
        (REPO_ROOT / "build" / "sim_core_cli.exe", '"build\\sim_core_cli.exe" --help'),
        (REPO_ROOT / "build" / "sim_core_cli", './build/sim_core_cli --help'),
        (REPO_ROOT / "apps" / "sim_core_cli.py", python_command("apps/sim_core_cli.py")),
        (REPO_ROOT / "apps" / "main.py", python_command("apps/main.py")),
    ]
    for path, command in candidates:
        if path.exists():
            return command

    if (REPO_ROOT / "CMakeLists.txt").exists():
        return "cmake -S . -B build && cmake --build build"

    return python_command("tools/repo_smoke_check.py")


class RunnerUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Sim_Core 실행 확인")
        self.geometry("900x620")
        self.minsize(760, 500)
        self.output_queue: queue.Queue[str] = queue.Queue()
        self.process: subprocess.Popen[str] | None = None

        self._build_widgets()
        self.after(80, self._drain_output)
        self._refresh_repo_info()

    def _build_widgets(self) -> None:
        outer = ttk.Frame(self, padding=16)
        outer.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(outer, text="Sim_Core 최신 체크아웃 실행", font=("Arial", 18, "bold"))
        title.pack(anchor=tk.W)

        info = ttk.Frame(outer)
        info.pack(fill=tk.X, pady=(12, 8))

        self.branch_var = tk.StringVar(value="-")
        self.commit_var = tk.StringVar(value="-")
        ttk.Label(info, text="브랜치:").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(info, textvariable=self.branch_var).grid(row=0, column=1, sticky=tk.W, padx=(6, 24))
        ttk.Label(info, text="커밋:").grid(row=0, column=2, sticky=tk.W)
        ttk.Label(info, textvariable=self.commit_var).grid(row=0, column=3, sticky=tk.W, padx=(6, 0))

        command_box = ttk.LabelFrame(outer, text="실행 명령", padding=10)
        command_box.pack(fill=tk.X, pady=(4, 10))

        self.command_var = tk.StringVar(value=detect_command())
        command_entry = ttk.Entry(command_box, textvariable=self.command_var)
        command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ttk.Button(command_box, text="자동 찾기", command=self._auto_detect).pack(side=tk.LEFT, padx=(8, 0))
        self.run_button = ttk.Button(command_box, text="실행", command=self._run)
        self.run_button.pack(side=tk.LEFT, padx=(8, 0))
        self.stop_button = ttk.Button(command_box, text="중지", command=self._stop, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=(8, 0))

        output_box = ttk.LabelFrame(outer, text="실행 결과", padding=10)
        output_box.pack(fill=tk.BOTH, expand=True)
        self.output = scrolledtext.ScrolledText(output_box, wrap=tk.WORD, font=("Consolas", 10))
        self.output.pack(fill=tk.BOTH, expand=True)

        footer = ttk.Frame(outer)
        footer.pack(fill=tk.X, pady=(10, 0))
        ttk.Button(footer, text="결과 지우기", command=lambda: self.output.delete("1.0", tk.END)).pack(side=tk.LEFT)
        ttk.Button(footer, text="저장소 정보 새로고침", command=self._refresh_repo_info).pack(side=tk.RIGHT)

    def _refresh_repo_info(self) -> None:
        self.branch_var.set(current_branch())
        self.commit_var.set(current_commit())

    def _auto_detect(self) -> None:
        self.command_var.set(detect_command())

    def _append(self, text: str) -> None:
        self.output.insert(tk.END, text)
        self.output.see(tk.END)

    def _run(self) -> None:
        if self.process is not None:
            messagebox.showinfo("실행 중", "이미 명령이 실행 중입니다.")
            return

        command = self.command_var.get().strip()
        if not command:
            messagebox.showwarning("명령 없음", "실행할 명령을 입력해 주세요.")
            return

        self._append(f"\n$ {command}\n")
        self.run_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        threading.Thread(target=self._worker, args=(command,), daemon=True).start()

    def _worker(self, command: str) -> None:
        try:
            self.process = subprocess.Popen(
                command,
                cwd=REPO_ROOT,
                shell=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                bufsize=1,
                env={**os.environ, "PYTHONUNBUFFERED": "1", "PYTHONUTF8": "1"},
            )
            assert self.process.stdout is not None
            for line in self.process.stdout:
                self.output_queue.put(line)
            return_code = self.process.wait()
            self.output_queue.put(f"\n[종료 코드: {return_code}]\n")
        except Exception as exc:
            self.output_queue.put(f"\n[실행 오류] {exc}\n")
        finally:
            self.process = None
            self.output_queue.put("__PROCESS_DONE__")

    def _stop(self) -> None:
        if self.process is not None:
            self.process.terminate()

    def _drain_output(self) -> None:
        try:
            while True:
                item = self.output_queue.get_nowait()
                if item == "__PROCESS_DONE__":
                    self.run_button.config(state=tk.NORMAL)
                    self.stop_button.config(state=tk.DISABLED)
                else:
                    self._append(item)
        except queue.Empty:
            pass
        self.after(80, self._drain_output)


if __name__ == "__main__":
    RunnerUI().mainloop()
