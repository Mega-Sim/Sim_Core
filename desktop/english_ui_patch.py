"""English-only presentation layer for the Sim_Core desktop workbench.

The feature modules intentionally keep their original implementation strings so the
English branch stays easy to rebase. This patch translates user-facing Qt text at
runtime and gives the application a dedicated modern Sim_Core icon.
"""
from __future__ import annotations

import re
from typing import Any

from PySide6.QtCore import QPointF, QRectF, QTimer, Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPainterPath, QPen, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGraphicsSimpleTextItem,
    QGraphicsTextItem,
    QGraphicsView,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QTabWidget,
    QTableWidget,
    QWidget,
)


_HANGUL_RE = re.compile(r"[가-힣]")

# Longest/specific phrases first. Substring replacement keeps dynamic values such as
# filenames, station counts and output paths intact.
_TRANSLATIONS = [
    ("현재 CAD를 선택한 상태에서는 자동 샘플 Facility로 대체하지 않습니다.", "When CAD is selected, the sample Facility is not used as a fallback."),
    ("경로 계산 중 CAD Graph 방향 또는 도면이 변경되어 이전 Graph의 결과를 화면에 연결하지 않았습니다. 현재 Graph로 다시 실행해 주세요.", "The CAD Graph direction or drawing changed during route calculation, so the previous result was discarded. Run the analysis again with the current Graph."),
    ("분석 중 CAD Graph가 변경되어 이전 Layout 결과를 연결하지 않았습니다. 현재 Graph로 다시 실행해 주세요.", "The CAD Graph changed during analysis, so the previous Layout result was discarded. Run the analysis again with the current Graph."),
    ("선택한 실제 FromTo CSV의 반송량을 그대로 방향성 최단경로에 누적했습니다. 원본 CSV는 수정하지 않고 분석 스냅샷만 별도 저장합니다.", "The transport volumes from the selected actual FromTo CSV were accumulated on directed shortest paths. The source CSV remains unchanged and only an analysis snapshot is saved separately."),
    ("입력한 시간당 반송을 방향성 최단경로에 누적했습니다. 초록색은 저사용, 빨간색은 고사용 Edge입니다.", "Hourly transport demand is accumulated on directed shortest paths. Green indicates low usage and red indicates high usage."),
    ("랜덤 FromTo 또는 연결한 실제 FromTo CSV를 선택해 방향성 최단경로 통행량 Heatmap을 분석합니다.", "Select Random FromTo or a connected Actual FromTo CSV to analyze directed shortest-path traffic as a heatmap."),
    ("현재 Facility의 Station과 방향성 Edge만으로 1시간 반송 Scenario를 만들고, 최단경로 통행량을 초록→빨강 Heatmap으로 표시합니다.", "Create a one-hour transport scenario from the current Facility stations and directed edges, then visualize shortest-path traffic as a green-to-red heatmap."),
    ("GitHub Actions에서 Windows EXE를 받으면 Core가 함께 포함됩니다.", "The Core is bundled with the Windows EXE package from GitHub Actions."),
    ("sim-core.exe를 찾지 못했습니다. GitHub Actions의 Windows 실행파일 패키지를 받거나 C++ Core를 먼저 빌드해 주세요.", "sim-core.exe was not found. Download the Windows executable package from GitHub Actions or build the C++ Core first."),
    ("Node, Edge, Station이 포함된 Facility JSON을 먼저 연결해 주세요.", "Connect a Facility JSON containing Nodes, Edges, and Stations first."),
    ("현재 CAD Graph를 Random LA Facility로 연결할 수 없습니다.", "The current CAD Graph cannot be connected as a Random LA Facility."),
    ("현재 CAD Graph · Random LA 연결 불가", "Current CAD Graph · Random LA unavailable"),
    ("자동 샘플 Facility는 사용하지 않습니다.", "The sample Facility is not used automatically."),
    ("Facility JSON을 연결하면 Station 기준 랜덤 수요를 생성할 수 있습니다.", "Connect a Facility JSON to generate station-based random demand."),
    ("Facility JSON을 연결하면 레이아웃이 표시됩니다.", "Connect a Facility JSON to display the layout."),
    ("DXF 파일을 선택하면 변환된 방향성 Graph가 표시됩니다.", "Select a DXF file to display the converted directed Graph."),
    ("DXF를 열어 방향성 Graph JSON으로 즉시 변환합니다.", "Open a DXF file and convert it directly into a directed Graph JSON."),
    ("Graph_Maker 참조 로직으로 LINE·ARC를 Node/방향성 Edge로 변환합니다.", "Convert LINE and ARC geometry into Nodes and directed Edges using the Graph_Maker reference logic."),
    ("휠 확대·축소, 드래그 이동, Node·Edge 마우스 확인을 지원합니다.", "Supports wheel zoom, drag pan, and mouse inspection of Nodes and Edges."),
    ("마우스 휠로 확대하고 드래그로 이동할 수 있습니다.", "Use the mouse wheel to zoom and drag to pan."),
    ("최단 경로, edge frequency, merge pressure와 Station 용량을 계산합니다.", "Calculates shortest paths, edge frequency, merge pressure, and station capacity."),
    ("차량·Job 상태 전이, manifest와 event trace를 생성합니다.", "Generates vehicle and job state transitions, a manifest, and an event trace."),
    ("화면과 입력 계약을 먼저 검증하며 Core 계산 결과로 사용하지 않습니다.", "Validates the UI and input contracts first; these are not used as authoritative Core results."),
    ("물류 흐름을 한 화면에서 실험합니다", "Experiment with material flow in one workspace"),
    ("실제 모델 데이터를 연결합니다", "Connect real model data"),
    ("실제 Core 분석 결과를 확인합니다", "Review actual Core analysis results"),
    ("결정론적 이벤트 실행을 제어합니다", "Control deterministic event execution"),
    ("다음 기능의 사용 경험을 먼저 검증합니다", "Preview and validate upcoming workflows"),
    ("레이아웃부터 병목 후보까지", "From layout to bottleneck candidates"),
    ("끊김 없이", "in one seamless workflow"),
    ("확인하세요.", "review everything."),
    ("현재 1–3차 Core와 DXF Graph 변환은 실제로 실행하고,", "The current Phase 1–3 Core and DXF Graph conversion run with real logic,"),
    ("ROI·Digital Twin은 미리 설계된 워크플로에서 입력 계약부터 준비합니다.", "while ROI and Digital Twin workflows begin with predesigned input contracts."),
    ("HTTP 전송 없이 선택한 로컬 파일을 직접 처리합니다.", "Processes selected local files directly without HTTP transfer."),
    ("Node, Edge, Station과 좌표 정보를 포함합니다.", "Contains Node, Edge, Station, and coordinate information."),
    ("차량, Job과 실행시간을 정의합니다.", "Defines vehicles, jobs, and simulation duration."),
    ("Station 간 시간당 예상 반송량입니다.", "Expected hourly transport volume between stations."),
    ("DXF Graph 변환 결과가 없습니다.", "No DXF Graph conversion result is available."),
    ("현재 랜덤 From-To 경로 계산이 끝날 때까지 기다려 주세요.", "Wait until the current Random FromTo route calculation finishes."),
    ("현재 Layout 정적 분석이 끝날 때까지 기다려 주세요.", "Wait until the current Layout static analysis finishes."),
    ("From-To CSV 카드에서 실제 반송 CSV를 먼저 연결해 주세요.", "Connect an actual transport CSV using the From-To CSV card first."),
    ("실제 FromTo 모드 · 위 From-To CSV 카드에서 실제 반송 CSV를 연결해 주세요.", "Actual FromTo mode · Connect an actual transport CSV using the From-To CSV card above."),
    ("실제 FromTo 기반 Layout 정적 분석 중…", "Running Layout static analysis using Actual FromTo…"),
    ("랜덤 From-To 생성 및 LA 정적분석 중…", "Generating Random FromTo and running LA static analysis…"),
    ("랜덤 From-To 및 LA 정적분석 완료", "Random FromTo and LA static analysis completed"),
    ("실제 FromTo Layout 정적 분석 완료", "Actual FromTo Layout static analysis completed"),
    ("실제 FromTo Layout 정적 분석 실패", "Actual FromTo Layout static analysis failed"),
    ("실제 FromTo 정적 분석 실패", "Actual FromTo static analysis failed"),
    ("랜덤 From-To 생성 실패", "Random FromTo generation failed"),
    ("경로 없는 Station", "Unreachable Stations"),
    ("Scenario/CSV 저장 완료", "Scenario/CSV saved"),
    ("분석 스냅샷 저장 완료", "Analysis snapshot saved"),
    ("원본 CSV 유지", "Source CSV unchanged"),
    ("원본 CSV", "Source CSV"),
    ("스냅샷", "Snapshot"),
    ("도달 가능한 방향성 경로를 계산하고 있습니다…", "Calculating reachable directed routes…"),
    ("실제 반송량을 방향성 최단경로에 누적하고 있습니다…", "Accumulating actual transport volume on directed shortest paths…"),
    ("경로 계산 중…", "Calculating routes…"),
    ("실제 FromTo 경로 계산 중…", "Calculating Actual FromTo routes…"),
    ("분석 결과 폐기", "Analysis Result Discarded"),
    ("분석 레이아웃 확인 필요", "Check Analysis Layout"),
    ("실제 FromTo CSV 필요", "Actual FromTo CSV Required"),
    ("Station 부족", "Insufficient Stations"),
    ("랜덤 From-To 생성에는 Station이 2개 이상 필요합니다.", "At least two Stations are required to generate Random FromTo demand."),
    ("Core 실행 파일 없음", "Core Executable Not Found"),
    ("Facility JSON과 Scenario JSON을 먼저 선택해 주세요.", "Select a Facility JSON and Scenario JSON first."),
    ("현재 Core 작업이 끝날 때까지 기다려 주세요.", "Wait until the current Core operation finishes."),
    ("CAD 원본에서 DXF 파일을 먼저 선택해 주세요.", "Select a DXF file from the CAD source first."),
    ("DXF geometry를 Graph로 변환하는 중입니다…", "Converting DXF geometry into a Graph…"),
    ("방향은 CAD geometry 기반 추정값입니다. 실제 OHT 운행 방향과 대조가 필요합니다.", "Directions are estimated from CAD geometry and should be checked against actual OHT travel directions."),
    ("CAD/Rail Graph를 먼저 변환해 주세요.", "Convert the CAD/Rail Graph first."),
    ("model.arc를 생성할 상위 폴더 선택", "Select Parent Folder for model.arc"),
    ("AutoMod model.arc 변환 완료", "AutoMod model.arc conversion completed"),
    ("선택한 Edge", "Selected Edges"),
    ("개의 방향을 반전했습니다.", " directions reversed."),
    ("Graph JSON 저장 시 변경 내용이 반영됩니다.", "Changes will be included when the Graph JSON is saved."),
    ("먼저 Edge를 클릭하거나 마우스로 영역을 드래그해 선택해 주세요.", "Click an Edge or drag a selection area first."),
    ("선택 영역에 반전 가능한 방향성 Edge가 없습니다.", "No reversible directed Edges are present in the selection."),
    ("Edge 클릭 또는 빈 영역에서 드래그: 블록 선택", "Click an Edge or drag on empty space: block selection"),
    ("마우스 드래그로 Edge 블록 선택 · 클릭으로 단일 Edge 선택 · 선택 후 방향 반전", "Drag to select an Edge block · Click to select one Edge · Reverse direction after selection"),
    ("방향성 Layout에서 실제 FromTo 경로를 찾을 수 없습니다:", "No route was found for the Actual FromTo pair in the directed Layout:"),
    ("실제 FromTo의 From Station이 Layout에 없습니다:", "The Actual FromTo From Station is not present in the Layout:"),
    ("실제 FromTo의 To Station이 Layout에 없습니다:", "The Actual FromTo To Station is not present in the Layout:"),
    ("실제 FromTo CSV를 찾을 수 없습니다:", "Actual FromTo CSV not found:"),
    ("실제 FromTo CSV에 헤더가 없습니다.", "The Actual FromTo CSV has no header."),
    ("실제 FromTo CSV에 분석할 데이터가 없습니다.", "The Actual FromTo CSV contains no data to analyze."),
    ("열이 없습니다. 현재 열:", " column is missing. Current columns:"),
    ("행의 From/To Station이 비어 있습니다.", " row has an empty From/To Station."),
    ("행 반송량이 숫자가 아닙니다:", " row transport volume is not numeric:"),
    ("행 반송량은 0 이상이어야 합니다.", " row transport volume must be zero or greater."),
    ("표시할 Node 좌표가 없습니다.", "No Node coordinates are available to display."),
    ("표시할 Node가 없습니다.", "No Nodes are available to display."),
    ("방향 미결정", "Direction unresolved"),
    ("통행량", "Traffic"),
    ("최대 Edge 대비", "of max Edge"),
    ("랜덤 From-To 생성 · LA 정적분석", "Random FromTo Generation · LA Static Analysis"),
    ("랜덤 From-To 생성 · 정적분석", "Generate Random FromTo · Static Analysis"),
    ("Layout 정적 분석 · 실제 FromTo Heatmap", "Layout Static Analysis · Actual FromTo Heatmap"),
    ("Layout 정적 분석 · 실제 FromTo", "Layout Static Analysis · Actual FromTo"),
    ("Layout 정적 분석", "Layout Static Analysis"),
    ("Random From-To · Edge 통행량 Heatmap", "Random FromTo · Edge Traffic Heatmap"),
    ("Random From-To LA 정적분석", "Random FromTo LA Static Analysis"),
    ("FromTo 분석 방식", "FromTo Analysis Mode"),
    ("랜덤 FromTo 정적분석 실행", "Run Random FromTo Static Analysis"),
    ("실제 FromTo 정적분석 실행", "Run Actual FromTo Static Analysis"),
    ("랜덤 FromTo", "Random FromTo"),
    ("실제 FromTo", "Actual FromTo"),
    ("분석 OD", "Analyzed OD"),
    ("유효 OD", "Valid OD"),
    ("생성 OD", "Generated OD"),
    ("도달 가능 OD", "Reachable OD"),
    ("사용 Edge", "Used Edges"),
    ("최대 Edge", "Max Edge"),
    ("생성 Vehicle", "Generated Vehicles"),
    ("총 반송량", "Total Transport"),
    ("저사용", "Low Usage"),
    ("최대 사용", "Maximum Usage"),
    ("생성 파일 폴더 열기", "Open Output Folder"),
    ("닫기", "Close"),
    ("분석 대상", "Analysis Target"),
    ("연결 불가", "Unavailable"),
    ("방향 추정", "Directions Resolved"),
    ("저장 전", "Not Saved"),
    ("저장 완료", "Saved"),
    ("변환 실패", "Conversion Failed"),
    ("변환 결과 필요", "Conversion Result Required"),
    ("DXF 파일 필요", "DXF File Required"),
    ("DXF 변환 실패", "DXF Conversion Failed"),
    ("Graph 저장 실패", "Graph Save Failed"),
    ("Graph JSON 저장 완료", "Graph JSON Saved"),
    ("Graph JSON 저장", "Save Graph JSON"),
    ("DXF 다시 변환", "Convert DXF Again"),
    ("CAD 변환 설정", "CAD Conversion Settings"),
    ("변환 결과 미리보기", "Conversion Preview"),
    ("DXF 파일을 선택해 주세요.", "Select a DXF file."),
    ("비우면 전체 LINE/ARC Layer", "Leave blank for all LINE/ARC layers"),
    ("도면 단위", "Drawing Unit"),
    ("Rail Layer (선택)", "Rail Layer (Optional)"),
    ("ARC 분할 수", "ARC Segments"),
    ("좌표 반올림", "Coordinate Rounding"),
    ("CAD 원본", "CAD Source"),
    ("DXF 변환", "DXF Conversion"),
    ("AutoMod 모델변환", "Convert to AutoMod"),
    ("AutoMod 변환 완료", "AutoMod Conversion Completed"),
    ("AutoMod 변환 실패", "AutoMod Conversion Failed"),
    ("그래프만 크게 보기", "Enlarge Graph"),
    ("선택 방향 반전", "Reverse Selected Direction"),
    ("CAD Graph 전체 화면", "CAD Graph Full Screen"),
    ("방향 반전", "Reverse Direction"),
    ("파일을 선택하세요", "Select a file"),
    ("파일 선택", "Select File"),
    ("입력 파일 선택", "Select Input File"),
    ("파일 오류", "File Error"),
    ("샘플 로드 실패", "Sample Load Failed"),
    ("샘플 불러오기", "Load Sample"),
    ("워크스페이스", "Workspace"),
    ("입력 · CAD", "Input · CAD"),
    ("Flow 분석", "Flow Analysis"),
    ("시뮬레이션", "Simulation"),
    ("데이터 연결하기", "Connect Data"),
    ("모델 검증", "Validate Model"),
    ("실제 연결", "Connected"),
    ("단계", "Stages"),
    ("교차·합류·정차점", "Junctions · merges · stops"),
    ("단방향 레일 구간", "Directed rail segments"),
    ("작업·주차 포트", "Work · parking ports"),
    ("From-To 수요", "From-To demand"),
    ("레이아웃 미리보기", "Layout Preview"),
    ("실제 데이터 연결", "Connect Real Data"),
    ("시간당 총 반송수", "Total Moves per Hour"),
    ("Random Seed (재현용)", "Random Seed (Reproducible)"),
    ("입력 검증", "Validate Input"),
    ("분석 실행", "Run Analysis"),
    ("Core 결과", "Core result"),
    ("도달 가능 경로", "Reachable routes"),
    ("사용률", "Utilization"),
    ("결정론적 DES 실행", "Deterministic DES Execution"),
    ("Scenario를 연결해 주세요.", "Connect a Scenario."),
    ("결정론적 실행 시작", "Start Deterministic Run"),
    ("아직 실행하지 않았습니다.", "Not run yet."),
    ("앞으로 만들 기능을 먼저 만져봅니다", "Preview Upcoming Features"),
    ("상위 위험 Edge 중심 축소 모델 요청 계약", "Reduced-model request contract focused on high-risk Edges"),
    ("동일 시드 기반 정책 비교 실험 계약", "Policy comparison experiment contract using the same seed"),
    ("USD·Isaac Sim 투영 요청 계약", "USD · Isaac Sim projection request contract"),
    ("Flow share와 merge pressure 기반 가설 계약", "Hypothesis contract based on flow share and merge pressure"),
    ("계약 생성", "Create Contract"),
    ("생성된 프로토타입 계약이 여기에 표시됩니다.", "Generated prototype contracts appear here."),
    ("실행 중", "Running"),
    ("입력 필요", "Input Required"),
    ("실행 결과", "Execution Result"),
    ("결과 해석 실패", "Result Parsing Failed"),
    ("종료 코드", "Exit code"),
    ("입니다. 화면 하단 로그를 확인해 주세요.", ". Check the log at the bottom of the screen."),
    ("실행 중…", "running…"),
    ("완료 · exit", "completed · exit"),
    ("Core 실행 가능", "Core Ready"),
    ("Core 미탑재", "Core Not Bundled"),
    ("차량", "Vehicles"),
    ("건", "Jobs"),
    ("대", "vehicles"),
    ("분석", "Analysis"),
    ("생성 실패", "Generation Failed"),
    ("분석 실패", "Analysis Failed"),
    ("생성 중", "Generating"),
    ("분석 중", "Analyzing"),
    ("원본", "Source"),
    ("완료", "Completed"),
    ("실패", "Failed"),
]

_TRANSLATIONS.sort(key=lambda item: len(item[0]), reverse=True)


def translate_text(value: str) -> str:
    """Translate known user-facing Korean fragments while preserving dynamic data."""

    if not value or not _HANGUL_RE.search(value):
        return value
    translated = value
    for source, target in _TRANSLATIONS:
        translated = translated.replace(source, target)
    translated = re.sub(r"(\d[\d,]*(?:\.\d+)?)개", r"\1", translated)
    return translated


def _translate_text_property(obj: Any, getter_name: str, setter_name: str) -> None:
    getter = getattr(obj, getter_name, None)
    setter = getattr(obj, setter_name, None)
    if not callable(getter) or not callable(setter):
        return
    try:
        current = getter()
    except Exception:
        return
    if not isinstance(current, str):
        return
    translated = translate_text(current)
    if translated != current:
        try:
            setter(translated)
        except Exception:
            pass


def _translate_graphics_view(view: QGraphicsView) -> None:
    scene = view.scene()
    if scene is None:
        return
    for item in scene.items():
        _translate_text_property(item, "toolTip", "setToolTip")
        if isinstance(item, QGraphicsSimpleTextItem):
            _translate_text_property(item, "text", "setText")
        elif isinstance(item, QGraphicsTextItem):
            _translate_text_property(item, "toPlainText", "setPlainText")


def _translate_widget_tree(root: QWidget) -> None:
    for widget in [root, *root.findChildren(QWidget)]:
        _translate_text_property(widget, "windowTitle", "setWindowTitle")
        _translate_text_property(widget, "toolTip", "setToolTip")
        _translate_text_property(widget, "statusTip", "setStatusTip")

        if isinstance(widget, (QLabel, QPushButton)):
            _translate_text_property(widget, "text", "setText")
        if isinstance(widget, QGroupBox):
            _translate_text_property(widget, "title", "setTitle")

        if isinstance(widget, QLineEdit):
            _translate_text_property(widget, "placeholderText", "setPlaceholderText")

        if isinstance(widget, QStatusBar):
            _translate_text_property(widget, "currentMessage", "showMessage")

        if isinstance(widget, QComboBox):
            for index in range(widget.count()):
                current = widget.itemText(index)
                translated = translate_text(current)
                if translated != current:
                    widget.setItemText(index, translated)

        if isinstance(widget, QTabWidget):
            for index in range(widget.count()):
                current = widget.tabText(index)
                translated = translate_text(current)
                if translated != current:
                    widget.setTabText(index, translated)

        if isinstance(widget, QTableWidget):
            for column in range(widget.columnCount()):
                item = widget.horizontalHeaderItem(column)
                if item is not None:
                    translated = translate_text(item.text())
                    if translated != item.text():
                        item.setText(translated)
            for row in range(widget.rowCount()):
                item = widget.verticalHeaderItem(row)
                if item is not None:
                    translated = translate_text(item.text())
                    if translated != item.text():
                        item.setText(translated)

        if isinstance(widget, QGraphicsView):
            _translate_graphics_view(widget)


def _translate_application() -> None:
    app = QApplication.instance()
    if app is None:
        return
    for widget in app.topLevelWidgets():
        _translate_widget_tree(widget)


def _build_app_icon() -> QIcon:
    """Create a crisp, modern CAD/flow icon without external binary assets."""

    pixmap = QPixmap(256, 256)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(QColor("#071621"))
    painter.drawRoundedRect(QRectF(12, 12, 232, 232), 52, 52)

    painter.setPen(QPen(QColor(58, 104, 125, 110), 2))
    for offset in (64, 96, 128, 160, 192):
        painter.drawLine(offset, 36, offset, 220)
        painter.drawLine(36, offset, 220, offset)

    path = QPainterPath(QPointF(48, 174))
    path.cubicTo(QPointF(88, 174), QPointF(82, 92), QPointF(126, 92))
    path.cubicTo(QPointF(166, 92), QPointF(158, 154), QPointF(210, 154))
    painter.setPen(QPen(QColor("#49E6D3"), 15, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    painter.setBrush(Qt.BrushStyle.NoBrush)
    painter.drawPath(path)

    painter.setPen(QPen(QColor("#D9FFFF"), 4))
    painter.setBrush(QColor("#0A3440"))
    for point in (QPointF(48, 174), QPointF(126, 92), QPointF(210, 154)):
        painter.drawEllipse(point, 14, 14)

    painter.setPen(QPen(QColor("#8AB8FF"), 6, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    painter.setBrush(QColor(16, 39, 66, 220))
    cube = QPainterPath(QPointF(98, 50))
    cube.lineTo(QPointF(128, 34))
    cube.lineTo(QPointF(158, 50))
    cube.lineTo(QPointF(128, 67))
    cube.closeSubpath()
    painter.drawPath(cube)
    painter.drawLine(QPointF(98, 50), QPointF(98, 78))
    painter.drawLine(QPointF(158, 50), QPointF(158, 78))
    painter.drawLine(QPointF(98, 78), QPointF(128, 95))
    painter.drawLine(QPointF(158, 78), QPointF(128, 95))
    painter.drawLine(QPointF(128, 67), QPointF(128, 95))

    painter.end()
    return QIcon(pixmap)


def install_english_ui(base_module: Any) -> None:
    """Install English-only UI translation and application branding."""

    cls = base_module.MainWindow
    if getattr(cls, "_english_ui_installed", False):
        return
    cls._english_ui_installed = True
    base_module.BRANCH_NAME = "agent/English-UI"

    original_init = cls.__init__

    def english_init(self: QMainWindow) -> None:
        original_init(self)

        icon = _build_app_icon()
        app = QApplication.instance()
        if app is not None:
            app.setApplicationDisplayName("Sim_Core Flow Workbench")
            app.setWindowIcon(icon)
        self.setWindowIcon(icon)

        _translate_application()
        timer = QTimer(self)
        timer.setInterval(160)
        timer.timeout.connect(_translate_application)
        timer.start()
        self._english_ui_translation_timer = timer

    cls.__init__ = english_init
