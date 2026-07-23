"""English presentation layer for the Applied Materials sharing branch.

This patch keeps the existing simulation, CAD conversion, Layout analysis, and
AutoMod export logic unchanged. It translates user-facing Qt text at runtime so
the same mainline feature set can be demonstrated in an English-only UI.
"""
from __future__ import annotations

import re
import sys
from typing import Any, Callable

from PySide6.QtWidgets import (
    QFileDialog as QtFileDialog,
    QLabel,
    QLineEdit,
    QMessageBox as QtMessageBox,
    QPlainTextEdit,
    QPushButton,
    QTableWidget,
    QWidget,
)


_EXACT = {
    "UI 프로토타입": "UI PROTOTYPE",
    "CORE 연결": "CORE CONNECTED",
    "파일을 선택하세요": "Select a file",
    "파일 선택": "Select File",
    "입력 파일 선택": "Select Input File",
    "Facility JSON을 연결하면 레이아웃이 표시됩니다.": "Connect a Facility JSON file to display the layout.",
    "DXF 파일을 선택하면 변환된 방향성 Graph가 표시됩니다.": "Select a DXF file to display the converted directed graph.",
    "DXF 또는 Rail 파일을 선택하면 방향성 Graph가 표시됩니다.": "Select a DXF or Rail file to display the directed graph.",
    "표시할 Node가 없습니다.": "No nodes are available to display.",
    "표시할 Node 좌표가 없습니다.": "No node coordinates are available to display.",
    "방향 미결정": "Direction unresolved",
    "워크스페이스": "Workspace",
    "입력 · CAD": "Inputs · CAD",
    "Flow 분석": "Flow Analysis",
    "시뮬레이션": "Simulation",
    "Sim_Core  /  워크스페이스": "Sim_Core  /  Workspace",
    "물류 흐름을 한 화면에서 실험합니다": "Explore material flow in one integrated workspace",
    "✦  샘플 불러오기": "✦  Load Sample",
    "▷  Flow 분석 실행": "▷  Run Flow Analysis",
    "데이터 연결하기": "Connect Data",
    "모델 검증": "Validate Model",
    "실제 데이터 연결": "Connect Model Data",
    "HTTP 전송 없이 선택한 로컬 파일을 직접 처리합니다.": "Selected local files are processed directly without HTTP transfer.",
    "CAD 원본": "CAD Source",
    "DXF 변환": "DXF Conversion",
    "랜덤 From-To 생성 · LA 정적분석": "Random From-To Generation · LA Static Analysis",
    "Layout 정적 분석": "Layout Static Analysis",
    "시간당 총 반송수": "Total Moves per Hour",
    "Random Seed (재현용)": "Random Seed (Reproducibility)",
    "랜덤 FromTo": "Random FromTo",
    "실제 FromTo": "Actual FromTo",
    "FromTo 분석 방식": "FromTo Analysis Mode",
    "랜덤 From-To 생성 · 정적분석": "Generate Random From-To · Static Analysis",
    "랜덤 FromTo 정적분석 실행": "Run Random FromTo Static Analysis",
    "실제 FromTo 정적분석 실행": "Run Actual FromTo Static Analysis",
    "CAD 변환 설정": "CAD Conversion Settings",
    "도면 단위": "Drawing Unit",
    "Rail Layer (선택)": "Rail Layer (Optional)",
    "ARC 분할 수": "ARC Segments",
    "좌표 반올림": "Coordinate Precision",
    "↻  DXF 다시 변환": "↻  Reconvert DXF",
    "Graph JSON 저장": "Save Graph JSON",
    "AutoMod 모델변환": "Convert to AutoMod",
    "변환 결과 미리보기": "Conversion Preview",
    "DXF 파일을 선택해 주세요.": "Select a DXF file.",
    "입력 검증": "Validate Inputs",
    "분석 실행": "Run Analysis",
    "사용률": "Utilization",
    "결정론적 DES 실행": "Deterministic DES Execution",
    "Simulation 실행": "Run Simulation",
    "Scenario를 연결해 주세요.": "Connect a Scenario file.",
    "결정론적 실행 시작": "Start Deterministic Run",
    "아직 실행하지 않았습니다.": "No run has been executed yet.",
    "앞으로 만들 기능을 먼저 만져봅니다": "Preview planned capabilities before implementation",
    "계약 생성": "Create Contract",
    "생성된 프로토타입 계약이 여기에 표시됩니다.": "Generated prototype contracts will appear here.",
    "실제 모델 데이터를 연결합니다": "Connect actual model data",
    "실제 Core 분석 결과를 확인합니다": "Review actual Core analysis results",
    "결정론적 이벤트 실행을 제어합니다": "Control deterministic event execution",
    "다음 기능의 사용 경험을 먼저 검증합니다": "Preview the user experience of upcoming capabilities",
    "샘플 로드 실패": "Sample Load Failed",
    "파일 오류": "File Error",
    "●  Core 실행 가능": "●  Core Ready",
    "●  Core 미탑재": "●  Core Not Installed",
    "경로 계산 중…": "Calculating Routes…",
    "생성 중": "Generation in Progress",
    "분석 중": "Analysis in Progress",
    "분석 레이아웃 확인 필요": "Layout Verification Required",
    "Station 부족": "Insufficient Stations",
    "분석 결과 폐기": "Analysis Result Discarded",
    "랜덤 From-To 생성 실패": "Random From-To Generation Failed",
    "실행 중": "Operation in Progress",
    "Core 실행 파일 없음": "Core Executable Not Found",
    "입력 필요": "Inputs Required",
    "결과 해석 실패": "Result Parsing Failed",
    "Core 실행 결과": "Core Execution Result",
    "DXF 파일 필요": "DXF File Required",
    "DXF 변환 실패": "DXF Conversion Failed",
    "변환 결과 필요": "Conversion Result Required",
    "Graph 저장 실패": "Graph Save Failed",
    "실제 FromTo CSV 필요": "Actual FromTo CSV Required",
    "실제 FromTo 분석 실패": "Actual FromTo Analysis Failed",
    "실제 FromTo 정적 분석 실패": "Actual FromTo Static Analysis Failed",
    "Rail 변환 실패": "Rail Conversion Failed",
    "방향 반전": "Reverse Direction",
    "▣  그래프만 크게 보기": "▣  Open Graph View",
    "⇄  선택 방향 반전": "⇄  Reverse Selected Directions",
    "닫기": "Close",
    "생성 파일 폴더 열기": "Open Output Folder",
    "Random From-To · Edge 통행량 Heatmap": "Random From-To · Edge Traffic Heatmap",
    "Layout 정적 분석 · 실제 FromTo Heatmap": "Layout Static Analysis · Actual FromTo Heatmap",
    "총 반송량": "Total Moves",
    "생성 OD": "Generated OD",
    "분석 OD": "Analyzed OD",
    "도달 가능 OD": "Reachable OD",
    "유효 OD": "Valid OD",
    "사용 Edge": "Used Edges",
    "최대 Edge": "Peak Edge",
    "생성 Vehicle": "Generated Vehicles",
    "원본 CSV": "Source CSV",
    "저사용 · 0": "Low Usage · 0",
    "최대 사용 · 100%": "Maximum Usage · 100%",
    "Sim_Core · Random From-To LA 정적분석": "Sim_Core · Random From-To LA Static Analysis",
    "Sim_Core · Layout 정적 분석 · 실제 FromTo": "Sim_Core · Layout Static Analysis · Actual FromTo",
    "Sim_Core · CAD Graph 전체 화면": "Sim_Core · Full CAD Graph View",
    "Edge 클릭 또는 빈 영역에서 드래그: 블록 선택": "Click an edge or drag on empty space to select a block",
    "마우스 드래그로 Edge 블록 선택 · 클릭으로 단일 Edge 선택 · 선택 후 방향 반전": "Drag to select an edge block · Click to select one edge · Reverse direction after selection",
    "JSON 최상위 값은 object여야 합니다.": "The top-level JSON value must be an object.",
}

_FRAGMENTS = (
    ("레이아웃부터 병목 후보까지", "From layout to bottleneck candidates"),
    ("끊김 없이", "in one continuous workflow"),
    ("확인하세요.", "explore the entire flow."),
    ("현재 1–3차 Core와 DXF Graph 변환은 실제로 실행하고,", "The current Phase 1–3 Core and DXF Graph conversion run with production logic,"),
    ("ROI·Digital Twin은 미리 설계된 워크플로에서 입력 계약부터 준비합니다.", "while ROI reduction and Digital Twin workflows are prepared through defined input contracts."),
    ("4 / 8 단계", "4 / 8 stages"),
    ("실제 연결", "Live Integration"),
    ("교차·합류·정차점", "Junctions · merges · stops"),
    ("단방향 레일 구간", "Directed rail segments"),
    ("작업·주차 포트", "Work · parking ports"),
    ("From-To 수요", "From-To demand"),
    ("레이아웃 미리보기", "Layout Preview"),
    ("마우스 휠로 확대하고 드래그로 이동할 수 있습니다.", "Use the mouse wheel to zoom and drag to pan."),
    ("Node, Edge, Station과 좌표 정보를 포함합니다.", "Contains Node, Edge, Station, and coordinate information."),
    ("차량, Job과 실행시간을 정의합니다.", "Defines vehicles, jobs, and runtime."),
    ("Station 간 시간당 예상 반송량입니다.", "Defines expected hourly moves between stations."),
    ("DXF를 열어 방향성 Graph JSON으로 즉시 변환합니다.", "Opens DXF and converts it directly into a directed Graph JSON."),
    ("랜덤 FromTo 또는 연결한 실제 FromTo CSV를 선택해 방향성 최단경로 통행량 Heatmap을 분석합니다.", "Analyze directed shortest-path traffic as a heatmap using either random FromTo demand or a connected actual FromTo CSV."),
    ("현재 Facility의 Station과 방향성 Edge만으로 1시간 반송 Scenario를 만들고, 최단경로 통행량을 초록→빨강 Heatmap으로 표시합니다.", "Build a one-hour transport scenario from Facility stations and directed edges, then visualize shortest-path traffic as a green-to-red heatmap."),
    ("Facility JSON을 연결하면 Station 기준 랜덤 수요를 생성할 수 있습니다.", "Connect a Facility JSON file to generate station-based random demand."),
    ("Graph_Maker 참조 로직으로 LINE·ARC를 Node/방향성 Edge로 변환합니다.", "Converts LINE and ARC geometry into nodes and directed edges using the Graph_Maker reference logic."),
    ("비우면 전체 LINE/ARC Layer", "Leave blank to use all LINE/ARC layers"),
    ("휠 확대·축소, 드래그 이동, Node·Edge 마우스 확인을 지원합니다.", "Supports wheel zoom, drag panning, and mouse inspection of nodes and edges."),
    ("최단 경로, edge frequency, merge pressure와 Station 용량을 계산합니다.", "Calculates shortest paths, edge frequency, merge pressure, and station capacity."),
    ("Core 결과", "Core result"),
    ("도달 가능 경로", "Reachable routes"),
    ("차량·Job 상태 전이, manifest와 event trace를 생성합니다.", "Generates vehicle/job state transitions, a manifest, and an event trace."),
    ("화면과 입력 계약을 먼저 검증하며 Core 계산 결과로 사용하지 않습니다.", "Validates screens and input contracts first; these are not used as authoritative Core results."),
    ("Flow share와 merge pressure 기반 가설 계약", "Hypothesis contract based on flow share and merge pressure"),
    ("상위 위험 Edge 중심 축소 모델 요청 계약", "Reduced-model request contract focused on highest-risk edges"),
    ("동일 시드 기반 정책 비교 실험 계약", "Policy comparison experiment contract using identical seeds"),
    ("USD·Isaac Sim 투영 요청 계약", "USD · Isaac Sim projection request contract"),
    ("분석 대상 · ", "Analysis target · "),
    ("실제 FromTo 분석 대상 · ", "Actual FromTo target · "),
    ("원본 CSV 유지", "Source CSV preserved"),
    ("자동 샘플 Facility는 사용하지 않습니다.", "The sample Facility is not used automatically."),
    ("현재 CAD Graph", "Current CAD Graph"),
    ("Random LA 연결 불가", "Random LA unavailable"),
    ("DXF Graph 변환 결과가 없습니다.", "No DXF Graph conversion result is available."),
    ("분석 대상", "Analysis target"),
    ("현재 CAD Graph를 Random LA Facility로 연결할 수 없습니다.", "The current CAD Graph cannot be connected as a Random LA Facility."),
    ("Node, Edge, Station이 포함된 Facility JSON을 먼저 연결해 주세요.", "Connect a Facility JSON containing Node, Edge, and Station data first."),
    ("현재 랜덤 From-To 경로 계산이 끝날 때까지 기다려 주세요.", "Wait until the current random From-To route calculation finishes."),
    ("현재 Layout 정적 분석이 끝날 때까지 기다려 주세요.", "Wait until the current Layout static analysis finishes."),
    ("현재 CAD를 선택한 상태에서는 자동 샘플 Facility로 대체하지 않습니다.", "When CAD is selected, the application does not substitute the sample Facility."),
    ("랜덤 From-To 생성에는 Station이 2개 이상 필요합니다.", "Random From-To generation requires at least two stations."),
    ("도달 가능한 방향성 경로를 계산하고 있습니다…", "Calculating reachable directed routes…"),
    ("랜덤 From-To 생성 및 LA 정적분석 중…", "Generating random From-To demand and running LA static analysis…"),
    ("경로 계산 중 CAD Graph 방향 또는 도면이 변경되어 이전 Graph의 결과를 화면에 연결하지 않았습니다. 현재 Graph로 다시 실행해 주세요.", "The CAD Graph direction or drawing changed during route calculation, so results from the previous graph were not applied. Run the analysis again with the current graph."),
    ("경로 없는 Station", "Stations without routes"),
    ("도달 가능 Station 쌍", "reachable station pairs"),
    ("Scenario/CSV 저장 완료", "Scenario/CSV saved"),
    ("랜덤 From-To 및 LA 정적분석 완료", "Random From-To and LA static analysis completed"),
    ("생성 실패 · ", "Generation failed · "),
    ("현재 Core 작업이 끝날 때까지 기다려 주세요.", "Wait until the current Core operation finishes."),
    ("sim-core.exe를 찾지 못했습니다. GitHub Actions의 Windows 실행파일 패키지를 받거나 C++ Core를 먼저 빌드해 주세요.", "sim-core.exe was not found. Download the Windows executable package from GitHub Actions or build the C++ Core first."),
    ("Facility JSON과 Scenario JSON을 먼저 선택해 주세요.", "Select Facility JSON and Scenario JSON first."),
    ("실행 중…", "running…"),
    ("완료 · exit", "completed · exit"),
    ("종료 코드 ", "Exit code "),
    ("입니다. 화면 하단 로그를 확인해 주세요.", ". Check the log at the bottom of the screen."),
    ("CAD 원본에서 DXF 파일을 먼저 선택해 주세요.", "Select a DXF file from CAD Source first."),
    ("DXF geometry를 Graph로 변환하는 중입니다…", "Converting DXF geometry into a graph…"),
    ("변환 실패", "Conversion failed"),
    ("방향 추정", "Directions resolved"),
    ("저장 전", "Not saved"),
    ("방향은 CAD geometry 기반 추정값입니다. 실제 OHT 운행 방향과 대조가 필요합니다.", "Directions are inferred from CAD geometry and should be verified against actual OHT travel directions."),
    ("DXF Graph 변환 완료", "DXF Graph conversion completed"),
    ("DXF를 먼저 변환해 주세요.", "Convert the DXF first."),
    ("저장 완료", "Saved"),
    ("Graph JSON 저장 완료", "Graph JSON saved"),
    ("GitHub Actions에서 Windows EXE를 받으면 Core가 함께 포함됩니다.", "The Core is included in the Windows EXE package from GitHub Actions."),
    ("실제 FromTo 모드 · 위 From-To CSV 카드에서 실제 반송 CSV를 연결해 주세요.", "Actual FromTo mode · Connect the actual transport CSV using the From-To CSV card above."),
    ("From-To CSV 카드에서 실제 반송 CSV를 먼저 연결해 주세요.", "Connect the actual transport CSV using the From-To CSV card first."),
    ("실제 FromTo 경로 계산 중…", "Calculating Actual FromTo Routes…"),
    ("실제 반송량을 방향성 최단경로에 누적하고 있습니다…", "Accumulating actual transport volume along directed shortest paths…"),
    ("실제 FromTo 기반 Layout 정적 분석 중…", "Running Layout static analysis using Actual FromTo data…"),
    ("분석 중 CAD Graph가 변경되어 이전 Layout 결과를 연결하지 않았습니다. 현재 Graph로 다시 실행해 주세요.", "The CAD Graph changed during analysis, so the previous Layout result was not applied. Run the analysis again with the current graph."),
    ("실제 FromTo Layout 정적 분석 완료", "Actual FromTo Layout static analysis completed"),
    ("실제 FromTo 분석 실패", "Actual FromTo analysis failed"),
    ("실제 FromTo Layout 정적 분석 실패", "Actual FromTo Layout static analysis failed"),
    ("선택한 실제 FromTo CSV의 반송량을 그대로 방향성 최단경로에 누적했습니다. 원본 CSV는 수정하지 않고 분석 스냅샷만 별도 저장합니다.", "The transport volumes from the selected Actual FromTo CSV were accumulated directly along directed shortest paths. The source CSV is preserved and only a separate analysis snapshot is saved."),
    ("입력한 시간당 반송을 방향성 최단경로에 누적했습니다. 초록색은 저사용, 빨간색은 고사용 Edge입니다.", "Hourly transport demand was accumulated along directed shortest paths. Green indicates low-use edges and red indicates high-use edges."),
    ("원본 CSV ", "Source CSV "),
    ("원본 유지", "source preserved"),
    ("스냅샷 ", "Snapshot "),
    ("분석 ", "Analysis "),
    ("실제 FromTo CSV에 분석할 데이터가 없습니다.", "The Actual FromTo CSV contains no data to analyze."),
    ("반송량", "Transport Volume"),
    ("실제 FromTo CSV에 헤더가 없습니다.", "The Actual FromTo CSV has no header row."),
    ("실제 FromTo의 From Station이 Layout에 없습니다:", "The Actual FromTo origin station does not exist in the Layout:"),
    ("실제 FromTo의 To Station이 Layout에 없습니다:", "The Actual FromTo destination station does not exist in the Layout:"),
    ("방향성 Layout에서 실제 FromTo 경로를 찾을 수 없습니다:", "No directed Layout route could be found for Actual FromTo:"),
    ("Rail geometry를 경량 Rail Graph로 불러오는 중입니다…", "Loading Rail geometry as a lightweight Rail Graph…"),
    ("Rail 변환 실패", "Rail conversion failed"),
    ("경량 Rail 준비 완료", "Lightweight Rail ready"),
    ("Rail Graph 변환 완료", "Rail Graph conversion completed"),
    ("CAD/Rail Graph를 먼저 변환해 주세요.", "Convert the CAD/Rail Graph first."),
    ("model.arc를 생성할 상위 폴더 선택", "Select Parent Folder for model.arc"),
    ("AutoMod 변환 실패", "AutoMod Conversion Failed"),
    ("AutoMod 변환 완료", "AutoMod conversion completed"),
    ("AutoMod model.arc 변환 완료", "AutoMod model.arc conversion completed"),
    ("먼저 Edge를 클릭하거나 마우스로 영역을 드래그해 선택해 주세요.", "Select edges first by clicking an edge or dragging a selection area."),
    ("선택 영역에 반전 가능한 방향성 Edge가 없습니다.", "The selection contains no directed edges that can be reversed."),
    ("선택한 Edge ", "Reversed "),
    ("개의 방향을 반전했습니다. Graph JSON 저장 시 변경 내용이 반영됩니다.", " selected edge directions. The changes will be included when the Graph JSON is saved."),
    ("통행량 ", "Traffic "),
    ("최대 Edge 대비 ", "of max edge "),
    ("분석 스냅샷 저장 완료", "Analysis snapshot saved"),
    ("실제 FromTo ", "Actual FromTo "),
    ("총 ", "Total "),
    ("개 OD", " OD"),
    ("개 연결", " connected"),
    ("개 제외", " excluded"),
    (" · 저장 전", " · Not saved"),
)

_PATTERNS = (
    (
        re.compile(r"실제 FromTo CSV에 (.+) 열이 없습니다\. 현재 열: (.+)"),
        lambda m: f"Actual FromTo CSV is missing the {m.group(1)} column. Current columns: {m.group(2)}",
    ),
    (
        re.compile(r"실제 FromTo CSV를 찾을 수 없습니다: (.+)"),
        lambda m: f"Actual FromTo CSV could not be found: {m.group(1)}",
    ),
    (
        re.compile(r"실제 FromTo CSV (\d+)행의 From/To Station이 비어 있습니다\."),
        lambda m: f"From/To Station is empty on row {m.group(1)} of the Actual FromTo CSV.",
    ),
    (
        re.compile(r"실제 FromTo CSV (\d+)행 반송량이 숫자가 아닙니다: (.+)"),
        lambda m: f"Transport volume on row {m.group(1)} of the Actual FromTo CSV is not numeric: {m.group(2)}",
    ),
    (
        re.compile(r"실제 FromTo CSV (\d+)행 반송량은 0 이상이어야 합니다\."),
        lambda m: f"Transport volume on row {m.group(1)} of the Actual FromTo CSV must be zero or greater.",
    ),
)


def _translate_text(value: Any) -> str:
    text = str(value)
    if not text:
        return text
    translated = _EXACT.get(text, text)
    for pattern, replacement in _PATTERNS:
        if pattern.search(translated):
            translated = pattern.sub(replacement, translated)
    for korean, english in _FRAGMENTS:
        translated = translated.replace(korean, english)
    translated = re.sub(r"(\d[\d,]*)개", r"\1", translated)
    translated = re.sub(r"(\d[\d,]*)\s*대", r"\1 vehicles", translated)
    translated = re.sub(r"(\d[\d,]*)\s*건", r"\1 jobs", translated)
    return translated


def _translate_scene_tooltips(root: QWidget) -> None:
    for view_name in ("network", "cad_graph_view", "_graph_popup_view"):
        view = getattr(root, view_name, None)
        scene = view.scene() if view is not None and hasattr(view, "scene") else None
        if scene is None:
            continue
        for item in scene.items():
            if hasattr(item, "toolTip") and hasattr(item, "setToolTip"):
                tooltip = item.toolTip()
                if tooltip:
                    item.setToolTip(_translate_text(tooltip))


def _translate_widget_tree(root: QWidget) -> None:
    root.setWindowTitle(_translate_text(root.windowTitle()))
    root.setToolTip(_translate_text(root.toolTip()))

    for widget in root.findChildren(QWidget):
        widget.setToolTip(_translate_text(widget.toolTip()))
        if isinstance(widget, QLabel):
            if widget.objectName() != "FileName":
                widget.setText(_translate_text(widget.text()))
        elif isinstance(widget, QPushButton):
            widget.setText(_translate_text(widget.text()))
        elif isinstance(widget, QLineEdit):
            widget.setPlaceholderText(_translate_text(widget.placeholderText()))
        elif isinstance(widget, QPlainTextEdit):
            widget.setPlaceholderText(_translate_text(widget.placeholderText()))
        elif isinstance(widget, QTableWidget):
            for column in range(widget.columnCount()):
                item = widget.horizontalHeaderItem(column)
                if item is not None:
                    item.setText(_translate_text(item.text()))
    _translate_scene_tooltips(root)


class _MessageBoxProxy:
    @staticmethod
    def information(parent: Any, title: str, text: str, *args: Any, **kwargs: Any) -> Any:
        return QtMessageBox.information(parent, _translate_text(title), _translate_text(text), *args, **kwargs)

    @staticmethod
    def warning(parent: Any, title: str, text: str, *args: Any, **kwargs: Any) -> Any:
        return QtMessageBox.warning(parent, _translate_text(title), _translate_text(text), *args, **kwargs)

    @staticmethod
    def critical(parent: Any, title: str, text: str, *args: Any, **kwargs: Any) -> Any:
        return QtMessageBox.critical(parent, _translate_text(title), _translate_text(text), *args, **kwargs)


class _FileDialogProxy:
    @staticmethod
    def getOpenFileName(parent: Any = None, caption: str = "", directory: str = "", filter: str = "", *args: Any, **kwargs: Any) -> Any:
        return QtFileDialog.getOpenFileName(parent, _translate_text(caption), directory, filter, *args, **kwargs)

    @staticmethod
    def getSaveFileName(parent: Any = None, caption: str = "", directory: str = "", filter: str = "", *args: Any, **kwargs: Any) -> Any:
        return QtFileDialog.getSaveFileName(parent, _translate_text(caption), directory, filter, *args, **kwargs)

    @staticmethod
    def getExistingDirectory(parent: Any = None, caption: str = "", directory: str = "", *args: Any, **kwargs: Any) -> Any:
        return QtFileDialog.getExistingDirectory(parent, _translate_text(caption), directory, *args, **kwargs)


def _replace_dialog_globals() -> None:
    for module in tuple(sys.modules.values()):
        if module is None:
            continue
        try:
            if getattr(module, "QMessageBox", None) is QtMessageBox:
                setattr(module, "QMessageBox", _MessageBoxProxy)
            if getattr(module, "QFileDialog", None) is QtFileDialog:
                setattr(module, "QFileDialog", _FileDialogProxy)
        except Exception:
            continue


def _wrap_method(cls: type, name: str) -> None:
    original = getattr(cls, name, None)
    if not callable(original) or getattr(original, "_applied_english_wrapped", False):
        return

    def wrapped(self: Any, *args: Any, **kwargs: Any) -> Any:
        result = original(self, *args, **kwargs)
        try:
            _translate_widget_tree(self)
            status_bar = self.statusBar() if hasattr(self, "statusBar") else None
            if status_bar is not None:
                current = status_bar.currentMessage()
                translated = _translate_text(current)
                if translated != current:
                    status_bar.showMessage(translated, 8000)
        except Exception:
            pass
        return result

    wrapped._applied_english_wrapped = True  # type: ignore[attr-defined]
    setattr(cls, name, wrapped)


def _wrap_graph_enhancer() -> None:
    module = sys.modules.get("graph_ui_enhancer")
    if module is None:
        return

    controller = getattr(module, "GraphSelectionController", None)
    if controller is not None:
        _wrap_method(controller, "reverse_selected")

    original_popup = getattr(module, "_open_graph_popup", None)
    if callable(original_popup) and not getattr(original_popup, "_applied_english_wrapped", False):
        def popup(window: Any, app_module: Any) -> Any:
            result = original_popup(window, app_module)
            dialog = getattr(window, "_graph_popup", None)
            if dialog is not None:
                _translate_widget_tree(dialog)
            return result

        popup._applied_english_wrapped = True  # type: ignore[attr-defined]
        module._open_graph_popup = popup


def install_applied_english_ui(base_module: Any) -> None:
    """Install the English-only presentation layer for the sharing branch."""

    cls = base_module.MainWindow
    if getattr(cls, "_applied_english_ui_installed", False):
        return
    cls._applied_english_ui_installed = True

    base_module.BRANCH_NAME = "feature/applied-materials-english"
    _replace_dialog_globals()
    _wrap_graph_enhancer()

    for method_name in (
        "build_ui",
        "show",
        "switch_page",
        "refresh",
        "generate_random_flow",
        "_random_flow_ready",
        "_random_flow_failed",
        "_random_flow_finished",
        "_set_layout_analysis_mode",
        "_actual_fromto_ready",
        "_actual_fromto_failed",
        "_actual_fromto_finished",
        "convert_cad_graph",
        "save_cad_graph",
        "save_automod_model",
        "run_core",
        "process_finished",
    ):
        _wrap_method(cls, method_name)
