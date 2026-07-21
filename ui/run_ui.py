#!/usr/bin/env python3
"""Sim_Core Flow Workbench local server.

The server intentionally uses only the Python standard library. It serves the
browser UI and exposes a narrow API that invokes the existing ``sim-core`` CLI
with uploaded model contents. Arbitrary paths and command-line arguments are
not accepted from the browser.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import shutil
import subprocess
import sys
import threading
import time
import uuid
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple
from urllib.parse import urlparse


UI_VERSION = "0.1.0"
SOURCE_BRANCH = "feature/4차-ui-workbench"
MAX_REQUEST_BYTES = 25 * 1024 * 1024
COMMAND_TIMEOUT_SECONDS = 120
MAX_LOG_CHARS = 250_000

UI_ROOT = Path(__file__).resolve().parent
WEB_ROOT = UI_ROOT / "web"
REPOSITORY_ROOT = UI_ROOT.parent
RUN_ROOT = REPOSITORY_ROOT / ".sim_core_ui" / "runs"


CAPABILITIES = [
    {
        "id": "canonical-preview",
        "name": "Canonical 레이아웃 미리보기",
        "stage": "available",
        "engine": "UI",
        "description": "Facility JSON의 node, edge, station을 2D 네트워크로 표시합니다.",
    },
    {
        "id": "model-validation",
        "name": "구조·시나리오 검증",
        "stage": "available",
        "engine": "sim-core validate",
        "description": "현재 C++ Core의 실제 검증 명령을 실행합니다.",
    },
    {
        "id": "flow-intelligence",
        "name": "Flow Intelligence",
        "stage": "available",
        "engine": "sim-core analyze",
        "description": "최단 경로, edge flow, merge pressure와 station capacity를 계산합니다.",
    },
    {
        "id": "des-run",
        "name": "결정론적 DES 실행",
        "stage": "available",
        "engine": "sim-core run",
        "description": "차량과 Job을 실행하고 event trace와 manifest를 생성합니다.",
    },
    {
        "id": "cad-import",
        "name": "CAD Import",
        "stage": "prototype",
        "engine": "계약 설계",
        "description": "파일·단위·레이어 매핑을 점검하지만 CAD geometry 변환기는 아직 연결되지 않았습니다.",
    },
    {
        "id": "bottleneck-intelligence",
        "name": "Bottleneck Intelligence",
        "stage": "prototype",
        "engine": "UI 추정",
        "description": "3차 관측값으로 UI 가설 점수를 미리 보여주며 Core 판정값은 아닙니다.",
    },
    {
        "id": "roi-reduction",
        "name": "ROI Reduction",
        "stage": "prototype",
        "engine": "계약 설계",
        "description": "관심 edge 선택과 축소 요청 manifest를 만들지만 모델 축소 엔진은 미연결입니다.",
    },
    {
        "id": "policy-ab",
        "name": "Policy A/B Test",
        "stage": "prototype",
        "engine": "계약 설계",
        "description": "비교 실험 조건을 구성하지만 교체형 policy runtime은 미연결입니다.",
    },
    {
        "id": "digital-twin",
        "name": "Digital Twin Projection",
        "stage": "prototype",
        "engine": "계약 설계",
        "description": "USD 투영 manifest를 구성하지만 USD/Isaac Sim adapter는 미연결입니다.",
    },
]


def find_sim_core() -> Optional[Path]:
    """Return the first executable sim-core candidate, if available."""
    candidates = []
    configured = os.environ.get("SIM_CORE_BIN")
    if configured:
        candidates.append(Path(configured).expanduser())
    candidates.extend(
        [
            REPOSITORY_ROOT / "build" / "sim-core",
            REPOSITORY_ROOT / "build" / "Release" / "sim-core",
            REPOSITORY_ROOT / "out" / "build" / "sim-core",
        ]
    )
    from_path = shutil.which("sim-core")
    if from_path:
        candidates.append(Path(from_path))
    for candidate in candidates:
        try:
            resolved = candidate.resolve()
            if resolved.is_file() and os.access(str(resolved), os.X_OK):
                return resolved
        except OSError:
            continue
    return None


def load_sample() -> Dict[str, Any]:
    sample_root = REPOSITORY_ROOT / "examples" / "cross_domain"
    paths = {
        "facility": sample_root / "facility.json",
        "scenario": sample_root / "scenario.json",
        "from_to": sample_root / "from_to.csv",
    }
    missing = [str(path.relative_to(REPOSITORY_ROOT)) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError("샘플 파일을 찾을 수 없습니다: " + ", ".join(missing))
    return {
        "facility": json.loads(paths["facility"].read_text(encoding="utf-8")),
        "scenario": json.loads(paths["scenario"].read_text(encoding="utf-8")),
        "from_to": paths["from_to"].read_text(encoding="utf-8-sig"),
        "names": {
            "facility": "examples/cross_domain/facility.json",
            "scenario": "examples/cross_domain/scenario.json",
            "from_to": "examples/cross_domain/from_to.csv",
        },
    }


def status_payload() -> Dict[str, Any]:
    binary = find_sim_core()
    sample_ready = True
    try:
        load_sample()
    except (OSError, ValueError, json.JSONDecodeError):
        sample_ready = False
    return {
        "ui_version": UI_VERSION,
        "source_branch": SOURCE_BRANCH,
        "engine": {
            "ready": binary is not None,
            "path": str(binary) if binary else None,
            "build_hint": "cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build --parallel",
        },
        "sample_ready": sample_ready,
        "capabilities": CAPABILITIES,
    }


def clean_old_runs(max_age_seconds: int = 7 * 24 * 60 * 60) -> None:
    if not RUN_ROOT.exists():
        return
    cutoff = time.time() - max_age_seconds
    for path in RUN_ROOT.iterdir():
        try:
            if path.is_dir() and path.stat().st_mtime < cutoff:
                shutil.rmtree(path)
        except OSError:
            continue


def require_text(payload: Dict[str, Any], key: str, *, allow_empty: bool = False) -> str:
    value = payload.get(key)
    if not isinstance(value, str):
        raise ValueError(f"{key} 입력이 문자열이 아닙니다.")
    if not allow_empty and not value.strip():
        raise ValueError(f"{key} 입력이 비어 있습니다.")
    return value


def write_input(run_dir: Path, name: str, content: str) -> Path:
    path = run_dir / name
    path.write_text(content, encoding="utf-8", newline="\n")
    return path


def execute(payload: Dict[str, Any]) -> Tuple[int, Dict[str, Any]]:
    action = payload.get("action")
    if action not in {"validate", "analyze", "run", "replay"}:
        raise ValueError("지원하지 않는 실행 요청입니다.")

    binary = find_sim_core()
    if binary is None:
        return HTTPStatus.SERVICE_UNAVAILABLE, {
            "ok": False,
            "error": "sim-core 실행 파일을 찾지 못했습니다.",
            "build_hint": status_payload()["engine"]["build_hint"],
        }

    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    run_id = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:8]
    run_dir = RUN_ROOT / run_id
    run_dir.mkdir(mode=0o700)

    command = [str(binary), action]
    result_file: Optional[Path] = None
    trace_file: Optional[Path] = None
    manifest_file: Optional[Path] = None

    if action in {"validate", "analyze", "run"}:
        facility = write_input(run_dir, "facility.json", require_text(payload, "facility"))
        scenario = write_input(run_dir, "scenario.json", require_text(payload, "scenario"))
        command.extend(["--facility", str(facility), "--scenario", str(scenario)])

    if action == "analyze":
        from_to = require_text(payload, "from_to", allow_empty=True)
        if from_to.strip():
            from_to_path = write_input(run_dir, "from_to.csv", from_to)
            command.extend(["--from-to-csv", str(from_to_path)])
        result_file = run_dir / "analysis-report.json"
        command.extend(["--output", str(result_file)])
    elif action == "run":
        output_dir = run_dir / "simulation"
        command.extend(["--output", str(output_dir)])
        trace_file = output_dir / "event_trace.jsonl"
        manifest_file = output_dir / "run_manifest.json"
    elif action == "replay":
        trace_file = write_input(run_dir, "event_trace.jsonl", require_text(payload, "trace"))
        command.extend(["--trace", str(trace_file)])

    started = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            cwd=str(REPOSITORY_ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=COMMAND_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        return HTTPStatus.REQUEST_TIMEOUT, {
            "ok": False,
            "run_id": run_id,
            "error": f"실행이 {COMMAND_TIMEOUT_SECONDS}초 제한을 초과했습니다.",
            "stdout": (error.stdout or "")[-MAX_LOG_CHARS:],
            "stderr": (error.stderr or "")[-MAX_LOG_CHARS:],
        }

    response: Dict[str, Any] = {
        "ok": completed.returncode == 0,
        "run_id": run_id,
        "action": action,
        "return_code": completed.returncode,
        "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
        "stdout": completed.stdout[-MAX_LOG_CHARS:],
        "stderr": completed.stderr[-MAX_LOG_CHARS:],
    }

    def read_json_if_present(path: Optional[Path]) -> Optional[Any]:
        if path and path.is_file():
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                return None
        return None

    if result_file:
        response["report"] = read_json_if_present(result_file)
    if manifest_file:
        response["manifest"] = read_json_if_present(manifest_file)
    if trace_file and trace_file.is_file() and action == "run":
        trace = trace_file.read_text(encoding="utf-8", errors="replace")
        response["trace"] = trace[-MAX_LOG_CHARS:]

    # A validation/analysis failure is a valid command result and must reach the UI.
    return HTTPStatus.OK, response


class WorkbenchHandler(BaseHTTPRequestHandler):
    server_version = "SimCoreWorkbench/" + UI_VERSION

    def log_message(self, format: str, *args: Any) -> None:
        sys.stderr.write("[Sim_Core UI] " + (format % args) + "\n")

    def _json(self, status: int, body: Dict[str, Any]) -> None:
        encoded = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(encoded)

    def _read_json(self) -> Dict[str, Any]:
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError as error:
            raise ValueError("잘못된 Content-Length입니다.") from error
        if length <= 0:
            raise ValueError("요청 본문이 비어 있습니다.")
        if length > MAX_REQUEST_BYTES:
            raise OverflowError("입력 데이터가 25 MB 제한을 초과했습니다.")
        raw = self.rfile.read(length)
        try:
            value = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError("요청 JSON을 해석할 수 없습니다.") from error
        if not isinstance(value, dict):
            raise ValueError("요청 JSON의 최상위 값은 object여야 합니다.")
        return value

    def _static(self, request_path: str) -> None:
        relative = "index.html" if request_path in {"", "/"} else request_path.lstrip("/")
        try:
            target = (WEB_ROOT / relative).resolve()
            target.relative_to(WEB_ROOT.resolve())
        except (OSError, ValueError):
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        if not target.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        data = target.read_bytes()
        mime, _ = mimetypes.guess_type(str(target))
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", (mime or "application/octet-stream") + ("; charset=utf-8" if mime and mime.startswith("text/") else ""))
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        path = urlparse(self.path).path
        try:
            if path == "/api/status":
                self._json(HTTPStatus.OK, status_payload())
            elif path == "/api/sample":
                self._json(HTTPStatus.OK, {"ok": True, **load_sample()})
            elif path.startswith("/api/"):
                self._json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "API를 찾을 수 없습니다."})
            else:
                self._static(path)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            self._json(HTTPStatus.INTERNAL_SERVER_ERROR, {"ok": False, "error": str(error)})

    def do_POST(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        path = urlparse(self.path).path
        if path != "/api/execute":
            self._json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "API를 찾을 수 없습니다."})
            return
        try:
            status, body = execute(self._read_json())
            self._json(status, body)
        except OverflowError as error:
            self._json(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, {"ok": False, "error": str(error)})
        except (OSError, ValueError) as error:
            self._json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": str(error)})
        except Exception as error:  # keep the local workbench responsive on unexpected failures
            self._json(HTTPStatus.INTERNAL_SERVER_ERROR, {"ok": False, "error": f"서버 오류: {error}"})


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sim_Core Flow Workbench")
    parser.add_argument("--host", default="127.0.0.1", help="기본값: 127.0.0.1")
    parser.add_argument("--port", type=int, default=8765, help="기본값: 8765")
    parser.add_argument("--no-browser", action="store_true", help="브라우저를 자동으로 열지 않습니다.")
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    clean_old_runs()
    server = ThreadingHTTPServer((args.host, args.port), WorkbenchHandler)
    actual_host, actual_port = server.server_address[:2]
    browse_host = "127.0.0.1" if actual_host in {"0.0.0.0", "::"} else actual_host
    url = f"http://{browse_host}:{actual_port}"
    print("Sim_Core Flow Workbench")
    print(f"UI: {url}")
    binary = find_sim_core()
    print(f"Core: {binary if binary else '미빌드 — UI 미리보기만 사용 가능'}")
    print("종료: Ctrl+C")

    if not args.no_browser:
        threading.Timer(0.35, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nUI를 종료합니다.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
