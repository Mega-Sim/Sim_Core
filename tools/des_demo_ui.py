#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import queue
import shutil
import subprocess
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, scrolledtext, ttk

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
OUTPUT = ROOT / "run-output-ui"
FACILITY = ROOT / "examples" / "single_line" / "facility.json"
SCENARIO = ROOT / "examples" / "single_line" / "scenario.json"


def exe(name: str) -> Path:
    suffix = ".exe" if os.name == "nt" else ""
    candidates = [
        BUILD / f"{name}{suffix}",
        BUILD / "Debug" / f"{name}{suffix}",
        BUILD / "Release" / f"{name}{suffix}",
    ]
    for path in candidates:
        if path.exists():
            return path
    return candidates[0]


def tool_path(name: str) -> str | None:
    return shutil.which(name)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sim_Core 1차 DES Demo")
        self.geometry("1050x720")
        self.q: queue.Queue[tuple[str, str]] = queue.Queue()
        self.running = False
        self._ui()
        self.after(100, self._drain)
        self._draw_route("IDLE")
        self._show_environment()

    def _ui(self):
        top = ttk.Frame(self, padding=12)
        top.pack(fill=tk.X)
        ttk.Label(top, text="Sim_Core 1차 DES Vertical Slice", font=("Arial", 18, "bold")).pack(side=tk.LEFT)
        ttk.Button(top, text="1. 빌드 + 7개 테스트", command=self.build_test).pack(side=tk.RIGHT, padx=4)
        ttk.Button(top, text="2. 샘플 실행", command=self.run_demo).pack(side=tk.RIGHT, padx=4)
        ttk.Button(top, text="3. Replay", command=self.replay).pack(side=tk.RIGHT, padx=4)

        summary = ttk.LabelFrame(self, text="샘플 시나리오", padding=10)
        summary.pack(fill=tk.X, padx=12, pady=(0, 8))
        self.status = tk.StringVar(value="대기")
        self.events = tk.StringVar(value="-")
        self.final_time = tk.StringVar(value="-")
        self.jobs = tk.StringVar(value="-")
        for i, (name, var) in enumerate([
            ("상태", self.status),
            ("이벤트", self.events),
            ("최종 시간", self.final_time),
            ("완료 Job", self.jobs),
        ]):
            ttk.Label(summary, text=f"{name}:").grid(row=0, column=i * 2, sticky="w", padx=(0, 4))
            ttk.Label(summary, textvariable=var, font=("Arial", 10, "bold")).grid(
                row=0, column=i * 2 + 1, sticky="w", padx=(0, 20)
            )

        self.canvas = tk.Canvas(self, height=180, bg="white")
        self.canvas.pack(fill=tk.X, padx=12, pady=4)

        paned = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
        left = ttk.LabelFrame(paned, text="Event Trace", padding=6)
        right = ttk.LabelFrame(paned, text="빌드 / 테스트 / 실행 로그", padding=6)
        paned.add(left, weight=1)
        paned.add(right, weight=2)

        self.trace = ttk.Treeview(left, columns=("time", "vehicle", "job", "state"), show="headings")
        for column, width in [("time", 90), ("vehicle", 90), ("job", 90), ("state", 120)]:
            self.trace.heading(column, text=column)
            self.trace.column(column, width=width)
        self.trace.pack(fill=tk.BOTH, expand=True)

        self.log = scrolledtext.ScrolledText(right, wrap=tk.WORD, font=("Consolas", 9))
        self.log.pack(fill=tk.BOTH, expand=True)

    def _show_environment(self):
        cmake = tool_path("cmake")
        ctest = tool_path("ctest")
        self._append("=== 실행 환경 확인 ===\n")
        self._append(f"Repository: {ROOT}\n")
        self._append(f"cmake: {cmake or 'NOT FOUND'}\n")
        self._append(f"ctest: {ctest or 'NOT FOUND'}\n")
        if not cmake or not ctest:
            self._append("\n[필수 도구 없음]\n")
            self._append("CMake가 설치되어 있고 PATH에 등록되어 있어야 C++ Sim_Core를 빌드할 수 있습니다.\n")
            self._append("Windows 터미널에서 'cmake --version'과 'ctest --version'이 실행되는지 확인해 주세요.\n")
            self._append("설치 후 이미 열려 있던 Git Bash/터미널은 닫고 새로 여는 것이 안전합니다.\n")
        self._append("\n")

    def _draw_route(self, state: str):
        canvas = self.canvas
        canvas.delete("all")
        y = 90
        xs = [100, 420, 850]
        labels = ["ST-START", "ST-PICKUP", "ST-DROPOFF"]
        canvas.create_line(xs[0], y, xs[2], y, width=5, arrow=tk.LAST)
        for x, label in zip(xs, labels):
            canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white", outline="black", width=2)
            canvas.create_text(x, y + 30, text=label)
        pos = {
            "TO_PICKUP": 260,
            "LOADING": 420,
            "TO_DROPOFF": 640,
            "UNLOADING": 850,
            "IDLE": 100,
        }.get(state, 100)
        canvas.create_oval(pos - 14, y - 42, pos + 14, y - 14, fill="black")
        canvas.create_text(pos, y - 58, text=f"OHT-001  {state}")

    def _append(self, text: str):
        self.log.insert(tk.END, text)
        self.log.see(tk.END)

    def _run_async(self, label, commands, done=None):
        if self.running:
            messagebox.showinfo("실행 중", "현재 작업이 끝난 뒤 다시 실행해 주세요.")
            return
        self.running = True
        self.status.set(label)
        self._append(f"\n=== {label} ===\n")

        def worker():
            ok = True
            try:
                for cmd in commands:
                    self.q.put(("log", "$ " + " ".join(map(str, cmd)) + "\n"))
                    try:
                        process = subprocess.run(
                            cmd,
                            cwd=ROOT,
                            text=True,
                            encoding="utf-8",
                            errors="replace",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            check=False,
                        )
                    except FileNotFoundError as exc:
                        missing = str(cmd[0]) if cmd else "unknown"
                        self.q.put((
                            "log",
                            f"[ERROR] 실행 파일을 찾을 수 없습니다: {missing}\n"
                            f"{exc}\n"
                            "필요한 도구가 설치되어 있고 PATH에 등록되어 있는지 확인해 주세요.\n"
                        ))
                        ok = False
                        break
                    except OSError as exc:
                        self.q.put(("log", f"[ERROR] 명령 실행 실패: {exc}\n"))
                        ok = False
                        break

                    self.q.put(("log", process.stdout + f"\n[exit={process.returncode}]\n"))
                    if process.returncode != 0:
                        ok = False
                        break
            except Exception as exc:
                self.q.put(("log", f"[ERROR] 예기치 않은 실행 오류: {exc}\n"))
                ok = False
            finally:
                self.q.put(("done", "1" if ok else "0"))
                if ok and done:
                    self.q.put((done, ""))

        threading.Thread(target=worker, daemon=True).start()

    def build_test(self):
        cmake = tool_path("cmake")
        ctest = tool_path("ctest")
        if not cmake or not ctest:
            missing = []
            if not cmake:
                missing.append("cmake")
            if not ctest:
                missing.append("ctest")
            self.status.set("빌드 도구 없음")
            messagebox.showerror(
                "CMake 필요",
                "다음 실행 파일을 PATH에서 찾지 못했습니다: " + ", ".join(missing) +
                "\n\nCMake 설치 후 새 터미널에서 cmake --version을 확인해 주세요."
            )
            self._show_environment()
            return

        self._run_async(
            "빌드 및 테스트 중",
            [
                [cmake, "-S", ".", "-B", "build"],
                [cmake, "--build", "build", "--config", "Release"],
                [ctest, "--test-dir", "build", "-C", "Release", "--output-on-failure"],
            ],
        )

    def run_demo(self):
        binary = exe("sim-core")
        if not binary.exists():
            messagebox.showwarning("빌드 필요", "먼저 '1. 빌드 + 7개 테스트'를 실행해 주세요.")
            return
        OUTPUT.mkdir(exist_ok=True)
        self._run_async(
            "샘플 실행 중",
            [[str(binary), "run", "--facility", str(FACILITY), "--scenario", str(SCENARIO), "--output", str(OUTPUT)]],
            "loadtrace",
        )

    def replay(self):
        binary = exe("sim-core")
        trace = OUTPUT / "event_trace.jsonl"
        if not binary.exists():
            messagebox.showwarning("빌드 필요", "먼저 '1. 빌드 + 7개 테스트'를 실행해 주세요.")
            return
        if not trace.exists():
            messagebox.showwarning("Trace 없음", "먼저 샘플 실행을 해 주세요.")
            return
        self._run_async("Replay 실행 중", [[str(binary), "replay", "--trace", str(trace)]], "loadtrace")

    def _load_trace(self):
        path = OUTPUT / "event_trace.jsonl"
        if not path.exists():
            return
        for item in self.trace.get_children():
            self.trace.delete(item)
        records = []
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        for record in records:
            time_value = record.get("simulation_time_us", record.get("time_us", "-"))
            vehicle = record.get("vehicle_id", "-")
            job = record.get("job_id", "-")
            state = record.get("vehicle_state", record.get("state", "-"))
            self.trace.insert("", tk.END, values=(time_value, vehicle, job, state))
        self.events.set(str(len(records)))
        if records:
            last = records[-1]
            time_value = last.get("simulation_time_us", last.get("time_us", 0))
            self.final_time.set(
                f"{time_value / 1_000_000:g} s" if isinstance(time_value, (int, float)) else str(time_value)
            )
            self._draw_route(last.get("vehicle_state", "IDLE"))
        manifest = OUTPUT / "run_manifest.json"
        if manifest.exists():
            try:
                data = json.loads(manifest.read_text(encoding="utf-8"))
                self.status.set(data.get("status", "COMPLETED"))
                self.events.set(str(data.get("processed_event_count", len(records))))
                self.final_time.set(f"{data.get('final_simulation_time_us', 0) / 1_000_000:g} s")
            except Exception:
                pass
        self.jobs.set("1 / 1")

    def _drain(self):
        try:
            while True:
                kind, data = self.q.get_nowait()
                if kind == "log":
                    self._append(data)
                elif kind == "done":
                    self.running = False
                    self.status.set("완료" if data == "1" else "실패")
                elif kind == "loadtrace":
                    self._load_trace()
        except queue.Empty:
            pass
        self.after(100, self._drain)


if __name__ == "__main__":
    App().mainloop()
