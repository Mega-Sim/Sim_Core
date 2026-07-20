#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import queue
import subprocess
import sys
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
    candidates = [BUILD / f"{name}{suffix}", BUILD / "Debug" / f"{name}{suffix}", BUILD / "Release" / f"{name}{suffix}"]
    for p in candidates:
        if p.exists():
            return p
    return candidates[0]


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
        for i, (name, var) in enumerate([("상태", self.status), ("이벤트", self.events), ("최종 시간", self.final_time), ("완료 Job", self.jobs)]):
            ttk.Label(summary, text=f"{name}:").grid(row=0, column=i*2, sticky="w", padx=(0,4))
            ttk.Label(summary, textvariable=var, font=("Arial", 10, "bold")).grid(row=0, column=i*2+1, sticky="w", padx=(0,20))

        self.canvas = tk.Canvas(self, height=180, bg="white")
        self.canvas.pack(fill=tk.X, padx=12, pady=4)

        paned = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
        left = ttk.LabelFrame(paned, text="Event Trace", padding=6)
        right = ttk.LabelFrame(paned, text="빌드 / 테스트 / 실행 로그", padding=6)
        paned.add(left, weight=1); paned.add(right, weight=2)
        self.trace = ttk.Treeview(left, columns=("time","vehicle","job","state"), show="headings")
        for c,w in [("time",90),("vehicle",90),("job",90),("state",120)]:
            self.trace.heading(c,text=c); self.trace.column(c,width=w)
        self.trace.pack(fill=tk.BOTH, expand=True)
        self.log = scrolledtext.ScrolledText(right, wrap=tk.WORD, font=("Consolas", 9))
        self.log.pack(fill=tk.BOTH, expand=True)

    def _draw_route(self, state: str):
        c=self.canvas; c.delete("all")
        y=90; xs=[100,420,850]; labels=["ST-START","ST-PICKUP","ST-DROPOFF"]
        c.create_line(xs[0],y,xs[2],y,width=5,arrow=tk.LAST)
        for x,l in zip(xs,labels):
            c.create_oval(x-10,y-10,x+10,y+10,fill="white",outline="black",width=2); c.create_text(x,y+30,text=l)
        pos={"TO_PICKUP":260,"LOADING":420,"TO_DROPOFF":640,"UNLOADING":850,"IDLE":100}.get(state,100)
        c.create_oval(pos-14,y-42,pos+14,y-14,fill="black"); c.create_text(pos,y-58,text=f"OHT-001  {state}")

    def _append(self, text):
        self.log.insert(tk.END,text); self.log.see(tk.END)

    def _run_async(self, label, commands, done=None):
        if self.running: messagebox.showinfo("실행 중","현재 작업이 끝난 뒤 다시 실행해 주세요."); return
        self.running=True; self.status.set(label); self._append(f"\n=== {label} ===\n")
        def worker():
            ok=True
            for cmd in commands:
                self.q.put(("log", "$ " + " ".join(map(str,cmd)) + "\n"))
                p=subprocess.run(cmd,cwd=ROOT,text=True,encoding="utf-8",errors="replace",stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                self.q.put(("log",p.stdout+f"\n[exit={p.returncode}]\n"))
                if p.returncode!=0: ok=False; break
            self.q.put(("done", "1" if ok else "0"))
            if ok and done: self.q.put((done,""))
        threading.Thread(target=worker,daemon=True).start()

    def build_test(self):
        self._run_async("빌드 및 테스트 중", [["cmake","-S",".","-B","build"],["cmake","--build","build","--config","Release"],["ctest","--test-dir","build","-C","Release","--output-on-failure"]])

    def run_demo(self):
        binary=exe("sim-core")
        if not binary.exists(): messagebox.showwarning("빌드 필요","먼저 '1. 빌드 + 7개 테스트'를 실행해 주세요."); return
        OUTPUT.mkdir(exist_ok=True)
        self._run_async("샘플 실행 중", [[str(binary),"run","--facility",str(FACILITY),"--scenario",str(SCENARIO),"--output",str(OUTPUT)]],"loadtrace")

    def replay(self):
        binary=exe("sim-core"); trace=OUTPUT/"event_trace.jsonl"
        if not trace.exists(): messagebox.showwarning("Trace 없음","먼저 샘플 실행을 해 주세요."); return
        self._run_async("Replay 실행 중", [[str(binary),"replay","--trace",str(trace)]],"loadtrace")

    def _load_trace(self):
        path=OUTPUT/"event_trace.jsonl"
        if not path.exists(): return
        for x in self.trace.get_children(): self.trace.delete(x)
        records=[]
        for line in path.read_text(encoding="utf-8").splitlines():
            try: records.append(json.loads(line))
            except json.JSONDecodeError: pass
        for r in records:
            t=r.get("simulation_time_us",r.get("time_us","-")); v=r.get("vehicle_id","-"); j=r.get("job_id","-"); s=r.get("vehicle_state",r.get("state","-"))
            self.trace.insert("",tk.END,values=(t,v,j,s))
        self.events.set(str(len(records)))
        if records:
            last=records[-1]; t=last.get("simulation_time_us",last.get("time_us",0)); self.final_time.set(f"{t/1_000_000:g} s" if isinstance(t,(int,float)) else str(t)); self._draw_route(last.get("vehicle_state","IDLE"))
        manifest=OUTPUT/"run_manifest.json"
        if manifest.exists():
            try:
                m=json.loads(manifest.read_text(encoding="utf-8")); self.status.set(m.get("status","COMPLETED")); self.events.set(str(m.get("processed_event_count",len(records)))); self.final_time.set(f"{m.get('final_simulation_time_us',0)/1_000_000:g} s")
            except Exception: pass
        self.jobs.set("1 / 1")

    def _drain(self):
        try:
            while True:
                kind,data=self.q.get_nowait()
                if kind=="log": self._append(data)
                elif kind=="done": self.running=False; self.status.set("완료" if data=="1" else "실패")
                elif kind=="loadtrace": self._load_trace()
        except queue.Empty: pass
        self.after(100,self._drain)

if __name__=="__main__": App().mainloop()
