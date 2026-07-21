"""Sim_Core native desktop workbench.

This application uses Qt widgets directly. It does not start a web server and
does not communicate over HTTP. The existing sim-core executable is launched
through QProcess so validation, analysis and simulation remain authoritative.
"""

from __future__ import annotations

import csv
import json
import math
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from PySide6.QtCore import QLineF, QProcess, QRectF, Qt, Signal
from PySide6.QtGui import QColor, QFont, QPainter, QPainterPath, QPen, QTextCursor
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QAbstractItemView,
    QFileDialog,
    QFrame,
    QGraphicsEllipseItem,
    QGraphicsPathItem,
    QGraphicsScene,
    QGraphicsSimpleTextItem,
    QGraphicsView,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


APP_VERSION = "0.2.0"
BRANCH_NAME = "feature/5차-native-desktop-workbench"


def runtime_root() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"))
    return Path(__file__).resolve().parents[1]


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def find_core() -> Optional[Path]:
    configured = os.environ.get("SIM_CORE_BIN")
    candidates: List[Path] = []
    if configured:
        candidates.append(Path(configured).expanduser())
    roots = [runtime_root(), repository_root()]
    for root in roots:
        candidates.extend(
            [
                root / "sim-core.exe",
                root / "sim-core",
                root / "build" / "Release" / "sim-core.exe",
                root / "build" / "Release" / "sim-core",
                root / "build" / "sim-core.exe",
                root / "build" / "sim-core",
            ]
        )
    located = shutil.which("sim-core")
    if located:
        candidates.append(Path(located))
    for candidate in candidates:
        try:
            if candidate.resolve().is_file():
                return candidate.resolve()
        except OSError:
            pass
    return None


def sample_root() -> Optional[Path]:
    for root in [runtime_root(), repository_root()]:
        candidate = root / "examples" / "cross_domain"
        if (candidate / "facility.json").is_file():
            return candidate
    return None


def output_root() -> Path:
    path = Path.home() / "Documents" / "Sim_Core" / "Runs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError("JSON 최상위 값은 object여야 합니다.")
    return value


def demand_count(path: Optional[Path], scenario: Optional[Dict[str, Any]]) -> int:
    if path and path.is_file():
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            return sum(1 for _ in csv.DictReader(stream))
    return len((scenario or {}).get("from_to_demands", []))


def button(text: str, kind: str = "secondary") -> QPushButton:
    widget = QPushButton(text)
    widget.setCursor(Qt.PointingHandCursor)
    widget.setProperty("kind", kind)
    widget.setMinimumHeight(40)
    return widget


def panel() -> QFrame:
    frame = QFrame()
    frame.setObjectName("Panel")
    return frame


def section_title(kicker: str, title: str, description: str = "") -> QWidget:
    wrapper = QWidget()
    layout = QVBoxLayout(wrapper)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(3)
    kick = QLabel(kicker)
    kick.setObjectName("Kicker")
    heading = QLabel(title)
    heading.setObjectName("SectionTitle")
    layout.addWidget(kick)
    layout.addWidget(heading)
    if description:
        desc = QLabel(description)
        desc.setObjectName("Muted")
        desc.setWordWrap(True)
        layout.addWidget(desc)
    return wrapper


def styled_label(text: str, object_name: str) -> QLabel:
    label = QLabel(text)
    label.setObjectName(object_name)
    return label


class MetricCard(QFrame):
    def __init__(self, title: str, accent: str, subtitle: str) -> None:
        super().__init__()
        self.setObjectName("MetricCard")
        self.setProperty("accent", accent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(17, 15, 17, 15)
        icon = QLabel("●")
        icon.setObjectName("MetricIcon")
        icon.setProperty("accent", accent)
        icon.setFixedWidth(30)
        texts = QVBoxLayout()
        texts.setSpacing(0)
        label = QLabel(title.upper())
        label.setObjectName("MetricLabel")
        self.value = QLabel("—")
        self.value.setObjectName("MetricValue")
        sub = QLabel(subtitle)
        sub.setObjectName("MetricSub")
        texts.addWidget(label)
        texts.addWidget(self.value)
        texts.addWidget(sub)
        layout.addWidget(icon)
        layout.addLayout(texts, 1)

    def set_value(self, value: Any) -> None:
        self.value.setText(str(value))


class FileCard(QFrame):
    selected = Signal(str)

    def __init__(self, key: str, icon: str, title: str, description: str, file_filter: str, prototype: bool = False) -> None:
        super().__init__()
        self.key = key
        self.file_filter = file_filter
        self.setObjectName("FileCard")
        self.setProperty("prototype", prototype)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(8)
        badge = QLabel("UI 프로토타입" if prototype else "CORE 연결")
        badge.setObjectName("PrototypeBadge" if prototype else "AvailableBadge")
        badge.setAlignment(Qt.AlignCenter)
        badge.setFixedWidth(92)
        icon_label = QLabel(icon)
        icon_label.setObjectName("FileIcon")
        icon_label.setAlignment(Qt.AlignCenter)
        name = QLabel(title)
        name.setObjectName("CardTitle")
        name.setAlignment(Qt.AlignCenter)
        desc = QLabel(description)
        desc.setObjectName("Muted")
        desc.setWordWrap(True)
        desc.setAlignment(Qt.AlignCenter)
        self.file_name = QLabel("파일을 선택하세요")
        self.file_name.setObjectName("FileName")
        self.file_name.setAlignment(Qt.AlignCenter)
        choose = button("파일 선택", "secondary")
        choose.clicked.connect(self.choose)
        layout.addWidget(badge, 0, Qt.AlignRight)
        layout.addWidget(icon_label)
        layout.addWidget(name)
        layout.addWidget(desc)
        layout.addStretch(1)
        layout.addWidget(choose)
        layout.addWidget(self.file_name)

    def choose(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "입력 파일 선택", "", self.file_filter)
        if path:
            self.file_name.setText(Path(path).name)
            self.file_name.setToolTip(path)
            self.selected.emit(path)

    def set_path(self, path: Optional[Path]) -> None:
        self.file_name.setText(path.name if path else "파일을 선택하세요")
        self.file_name.setToolTip(str(path) if path else "")


class NetworkView(QGraphicsView):
    def __init__(self) -> None:
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.setFrameShape(QFrame.NoFrame)
        self.setMinimumHeight(400)
        self.setObjectName("NetworkView")

    def drawBackground(self, painter: QPainter, rect: QRectF) -> None:  # noqa: N802
        painter.fillRect(rect, QColor("#07131d"))
        painter.setPen(QPen(QColor(38, 65, 79, 80), 0))
        step = 42
        left = math.floor(rect.left() / step) * step
        top = math.floor(rect.top() / step) * step
        x = left
        while x < rect.right():
            painter.drawLine(QLineF(x, rect.top(), x, rect.bottom()))
            x += step
        y = top
        while y < rect.bottom():
            painter.drawLine(QLineF(rect.left(), y, rect.right(), y))
            y += step

    def wheelEvent(self, event) -> None:  # type: ignore[no-untyped-def]
        factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(factor, factor)

    def set_model(self, facility: Optional[Dict[str, Any]], analysis: Optional[Dict[str, Any]] = None) -> None:
        scene = self.scene()
        scene.clear()
        if not facility:
            label = scene.addText("Facility JSON을 연결하면 레이아웃이 표시됩니다.")
            label.setDefaultTextColor(QColor("#78909d"))
            return
        nodes = facility.get("nodes", [])
        positions = {
            item.get("id"): item.get("position_um", {})
            for item in nodes
            if item.get("id") and item.get("position_um")
        }
        if not positions:
            return
        xs = [float(pos.get("x", 0)) for pos in positions.values()]
        ys = [float(pos.get("y", 0)) for pos in positions.values()]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        scale = 900.0 / max(max_x - min_x, max_y - min_y, 1.0)

        def point(raw: Dict[str, Any]) -> tuple[float, float]:
            return ((float(raw.get("x", 0)) - min_x) * scale, -(float(raw.get("y", 0)) - min_y) * scale)

        flow = {item.get("edge_id"): item for item in (analysis or {}).get("edge_flows", [])}
        for edge in facility.get("edges", []):
            polyline = edge.get("polyline_um", [])
            if len(polyline) < 2:
                continue
            path = QPainterPath()
            first = point(polyline[0])
            path.moveTo(*first)
            for raw in polyline[1:]:
                path.lineTo(*point(raw))
            observation = flow.get(edge.get("id"), {})
            share = max(0.0, min(1.0, float(observation.get("flow_share", 0))))
            color = QColor.fromHsvF((184 - 152 * share) / 360.0, 0.78, 0.76)
            item = QGraphicsPathItem(path)
            item.setPen(QPen(color if observation else QColor("#315568"), 2.5 + share * 7, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            item.setToolTip(
                f"{edge.get('id', '')}\n{edge.get('from_node_id', '')} → {edge.get('to_node_id', '')}"
                + (f"\n{observation.get('expected_moves_per_hour', 0):.1f} moves/h" if observation else "")
            )
            scene.addItem(item)
        for node_id, raw in positions.items():
            x, y = point(raw)
            dot = QGraphicsEllipseItem(x - 3, y - 3, 6, 6)
            dot.setBrush(QColor("#315568"))
            dot.setPen(QPen(QColor("#719bad"), 1))
            dot.setToolTip(node_id)
            scene.addItem(dot)
        for station in facility.get("stations", []):
            raw = station.get("position_um") or positions.get(station.get("attachment_node_id"))
            if not raw:
                continue
            x, y = point(raw)
            dot = QGraphicsEllipseItem(x - 8, y - 8, 16, 16)
            dot.setBrush(QColor("#071019"))
            dot.setPen(QPen(QColor("#43e4d3"), 2.5))
            dot.setToolTip(f"{station.get('id')} · {station.get('operation_type')}")
            scene.addItem(dot)
            text = QGraphicsSimpleTextItem(str(station.get("id", "")))
            text.setBrush(QColor("#a9c0cb"))
            text.setFont(QFont("Segoe UI", 8, QFont.Weight.DemiBold))
            text.setPos(x + 10, y - 20)
            scene.addItem(text)
        bounds = scene.itemsBoundingRect().adjusted(-50, -50, 50, 50)
        scene.setSceneRect(bounds)
        self.resetTransform()
        self.fitInView(bounds, Qt.KeepAspectRatio)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Sim_Core · Flow Workbench")
        self.resize(1480, 920)
        self.setMinimumSize(1120, 720)
        self.facility_path: Optional[Path] = None
        self.scenario_path: Optional[Path] = None
        self.demand_path: Optional[Path] = None
        self.cad_path: Optional[Path] = None
        self.facility: Optional[Dict[str, Any]] = None
        self.scenario: Optional[Dict[str, Any]] = None
        self.analysis: Optional[Dict[str, Any]] = None
        self.last_manifest: Optional[Dict[str, Any]] = None
        self.core = find_core()
        self.current_action = ""
        self.current_output: Optional[Path] = None
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.SeparateChannels)
        self.process.readyReadStandardOutput.connect(self.capture_stdout)
        self.process.readyReadStandardError.connect(self.capture_stderr)
        self.process.finished.connect(self.process_finished)
        self.build_ui()
        self.setStyleSheet(STYLESHEET)
        self.load_sample()
        self.refresh()

    def build_ui(self) -> None:
        root = QWidget()
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)
        root_layout.addWidget(self.build_sidebar())
        body = QWidget()
        body.setObjectName("Body")
        body_layout = QVBoxLayout(body)
        body_layout.setContentsMargins(28, 20, 28, 25)
        body_layout.setSpacing(18)
        body_layout.addWidget(self.build_topbar())
        self.pages = QStackedWidget()
        self.pages.addWidget(self.build_dashboard())
        self.pages.addWidget(self.build_inputs())
        self.pages.addWidget(self.build_analysis())
        self.pages.addWidget(self.build_simulation())
        self.pages.addWidget(self.build_future())
        body_layout.addWidget(self.pages, 1)
        root_layout.addWidget(body, 1)
        self.setCentralWidget(root)

    def build_sidebar(self) -> QWidget:
        side = QFrame()
        side.setObjectName("Sidebar")
        side.setFixedWidth(242)
        layout = QVBoxLayout(side)
        layout.setContentsMargins(18, 25, 18, 19)
        brand = QLabel("⬡  SIM_CORE\n     Flow Workbench")
        brand.setObjectName("Brand")
        layout.addWidget(brand)
        layout.addSpacing(24)
        self.nav_buttons: List[QPushButton] = []
        entries = [("⌂", "워크스페이스"), ("⇧", "입력 · CAD"), ("⌁", "Flow 분석"), ("▶", "시뮬레이션"), ("◇", "Future Lab")]
        for index, (icon, text) in enumerate(entries):
            nav = QPushButton(f"{icon}   {text}")
            nav.setObjectName("NavButton")
            nav.setCheckable(True)
            nav.setCursor(Qt.PointingHandCursor)
            nav.clicked.connect(lambda checked=False, page=index: self.switch_page(page))
            self.nav_buttons.append(nav)
            layout.addWidget(nav)
        self.nav_buttons[0].setChecked(True)
        layout.addStretch(1)
        self.core_card = QFrame()
        self.core_card.setObjectName("CoreCard")
        card_layout = QVBoxLayout(self.core_card)
        card_layout.setContentsMargins(13, 12, 13, 12)
        self.core_status = QLabel()
        self.core_status.setObjectName("CoreStatus")
        self.core_path_label = QLabel()
        self.core_path_label.setObjectName("TinyMuted")
        self.core_path_label.setWordWrap(True)
        card_layout.addWidget(self.core_status)
        card_layout.addWidget(self.core_path_label)
        layout.addWidget(self.core_card)
        footer = QLabel(f"Desktop v{APP_VERSION}\n{BRANCH_NAME}")
        footer.setObjectName("SidebarFooter")
        layout.addWidget(footer)
        return side

    def build_topbar(self) -> QWidget:
        bar = QWidget()
        layout = QHBoxLayout(bar)
        layout.setContentsMargins(0, 0, 0, 12)
        titles = QVBoxLayout()
        self.breadcrumb = QLabel("Sim_Core  /  워크스페이스")
        self.breadcrumb.setObjectName("Breadcrumb")
        self.page_title = QLabel("물류 흐름을 한 화면에서 실험합니다")
        self.page_title.setObjectName("PageTitle")
        titles.addWidget(self.breadcrumb)
        titles.addWidget(self.page_title)
        sample = button("✦  샘플 불러오기", "secondary")
        sample.clicked.connect(self.load_sample)
        run = button("▷  Flow 분석 실행", "primary")
        run.clicked.connect(lambda: self.run_core("analyze"))
        layout.addLayout(titles)
        layout.addStretch(1)
        layout.addWidget(sample)
        layout.addWidget(run)
        return bar

    def build_dashboard(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)
        hero = panel()
        hero_layout = QHBoxLayout(hero)
        hero_layout.setContentsMargins(30, 25, 30, 25)
        title = QLabel("레이아웃부터 병목 후보까지\n<font color='#43e4d3'>끊김 없이</font> 확인하세요.")
        title.setObjectName("HeroTitle")
        title.setTextFormat(Qt.RichText)
        desc = QLabel("현재 1–3차 Core는 실제로 실행하고, CAD·ROI·Digital Twin은\n미리 설계된 워크플로에서 입력 계약부터 준비합니다.")
        desc.setObjectName("Muted")
        copy = QVBoxLayout()
        copy.addWidget(styled_label("MODEL CONTROL CENTER", "Kicker"))
        copy.addWidget(title)
        copy.addWidget(desc)
        actions = QHBoxLayout()
        connect = button("데이터 연결하기", "primary")
        connect.clicked.connect(lambda: self.switch_page(1))
        validate = button("모델 검증", "secondary")
        validate.clicked.connect(lambda: self.run_core("validate"))
        actions.addWidget(connect)
        actions.addWidget(validate)
        actions.addStretch(1)
        copy.addLayout(actions)
        orbit = QLabel("<b style='font-size:36px'>3</b> / 8 단계<br><font color='#43e4d3'>Core 연결</font>")
        orbit.setObjectName("Orbit")
        orbit.setAlignment(Qt.AlignCenter)
        orbit.setFixedSize(150, 150)
        hero_layout.addLayout(copy, 1)
        hero_layout.addWidget(orbit)
        layout.addWidget(hero)
        metrics = QHBoxLayout()
        self.metric_nodes = MetricCard("Nodes", "cyan", "교차·합류·정차점")
        self.metric_edges = MetricCard("Edges", "blue", "단방향 레일 구간")
        self.metric_stations = MetricCard("Stations", "violet", "작업·주차 포트")
        self.metric_demands = MetricCard("Demand", "green", "From-To 수요")
        for card in [self.metric_nodes, self.metric_edges, self.metric_stations, self.metric_demands]:
            metrics.addWidget(card)
        layout.addLayout(metrics)
        network_panel = panel()
        network_layout = QVBoxLayout(network_panel)
        network_layout.setContentsMargins(20, 18, 20, 18)
        network_layout.addWidget(section_title("CANONICAL NETWORK", "레이아웃 미리보기", "마우스 휠로 확대하고 드래그로 이동할 수 있습니다."))
        self.network = NetworkView()
        network_layout.addWidget(self.network, 1)
        layout.addWidget(network_panel, 1)
        return page

    def build_inputs(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)
        layout.addWidget(section_title("INPUT CONTRACT", "실제 데이터 연결", "HTTP 전송 없이 선택한 로컬 파일을 직접 처리합니다."))
        cards = QHBoxLayout()
        self.file_cards: Dict[str, FileCard] = {}
        definitions = [
            ("facility", "{ }", "Facility JSON", "Node, Edge, Station과 좌표 정보를 포함합니다.", "JSON (*.json)", False),
            ("scenario", "▷", "Scenario JSON", "차량, Job과 실행시간을 정의합니다.", "JSON (*.json)", False),
            ("demand", "≋", "From-To CSV", "Station 간 시간당 예상 반송량입니다.", "CSV (*.csv)", False),
            ("cad", "⌑", "CAD 원본", "DXF·DWG·STEP Import 계약을 준비합니다.", "CAD (*.dxf *.dwg *.step *.stp *.ifc)", True),
        ]
        for definition in definitions:
            card = FileCard(*definition)
            card.selected.connect(lambda path, key=definition[0]: self.select_file(key, path))
            self.file_cards[definition[0]] = card
            cards.addWidget(card)
        layout.addLayout(cards, 1)
        contract = panel()
        form = QGridLayout(contract)
        form.setContentsMargins(22, 19, 22, 19)
        form.addWidget(section_title("CAD ADAPTER CONTRACT", "CAD 레이어 매핑", "현재는 계약 생성 단계이며 geometry 변환기는 이후 Core에 연결합니다."), 0, 0, 1, 4)
        self.cad_unit = QComboBox(); self.cad_unit.addItems(["millimeter", "meter", "micrometer", "inch"])
        self.rail_layer = QLineEdit("OHT_RAIL_CENTER")
        self.station_layer = QLineEdit("OHT_STATION")
        self.direction_layer = QLineEdit("OHT_DIRECTION")
        for column, (name, field) in enumerate([("도면 단위", self.cad_unit), ("Rail 중심선 Layer", self.rail_layer), ("Station Layer", self.station_layer), ("진행방향 Layer", self.direction_layer)]):
            form.addWidget(styled_label(name, "FieldLabel"), 1, column)
            form.addWidget(field, 2, column)
        save = button("Import 계약 저장", "secondary")
        save.clicked.connect(self.save_cad_contract)
        form.addWidget(save, 3, 3)
        layout.addWidget(contract)
        return page

    def build_analysis(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        header = QHBoxLayout()
        header.addWidget(section_title("A2 + A3 ACTUAL CORE", "Cross-Domain · Flow Intelligence", "최단 경로, edge frequency, merge pressure와 Station 용량을 계산합니다."))
        header.addStretch(1)
        validate = button("입력 검증", "secondary"); validate.clicked.connect(lambda: self.run_core("validate"))
        analyze = button("분석 실행", "primary"); analyze.clicked.connect(lambda: self.run_core("analyze"))
        header.addWidget(validate); header.addWidget(analyze)
        layout.addLayout(header)
        stats = QHBoxLayout()
        self.analysis_status_card = MetricCard("Status", "green", "Core 결과")
        self.route_card = MetricCard("Routes", "cyan", "도달 가능 경로")
        self.top_flow_card = MetricCard("Top Flow", "violet", "moves / hour")
        self.merge_card = MetricCard("Max Merge", "blue", "pressure / hour")
        for card in [self.analysis_status_card, self.route_card, self.top_flow_card, self.merge_card]: stats.addWidget(card)
        layout.addLayout(stats)
        tables = QHBoxLayout()
        self.edge_table = self.make_table(["Edge", "Moves/h", "Share", "Demand"])
        self.station_table = self.make_table(["Station", "Peak", "사용률", "Margin"])
        for title, table in [("EDGE FLOW RANKING", self.edge_table), ("STATION CAPACITY", self.station_table)]:
            frame = panel(); box = QVBoxLayout(frame); box.setContentsMargins(18, 15, 18, 15)
            box.addWidget(styled_label(title, "Kicker")); box.addWidget(table)
            tables.addWidget(frame)
        layout.addLayout(tables, 1)
        self.analysis_log = QPlainTextEdit()
        self.analysis_log.setReadOnly(True)
        self.analysis_log.setObjectName("Terminal")
        self.analysis_log.setPlaceholderText("$ sim-core analyze …")
        layout.addWidget(self.analysis_log, 1)
        return page

    def build_simulation(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        header = QHBoxLayout()
        header.addWidget(section_title("A1 ACTUAL CORE", "결정론적 DES 실행", "차량·Job 상태 전이, manifest와 event trace를 생성합니다."))
        header.addStretch(1)
        run = button("Simulation 실행", "primary"); run.clicked.connect(lambda: self.run_core("run")); header.addWidget(run)
        layout.addLayout(header)
        content = QHBoxLayout()
        config = panel(); config_layout = QVBoxLayout(config); config_layout.setContentsMargins(21, 18, 21, 18)
        config_layout.addWidget(styled_label("RUN CONFIGURATION", "Kicker"))
        self.sim_config = QLabel("Scenario를 연결해 주세요.")
        self.sim_config.setObjectName("Definition")
        self.sim_config.setWordWrap(True)
        config_layout.addWidget(self.sim_config)
        config_layout.addStretch(1)
        start = button("결정론적 실행 시작", "primary"); start.clicked.connect(lambda: self.run_core("run")); config_layout.addWidget(start)
        result = panel(); result_layout = QVBoxLayout(result); result_layout.setContentsMargins(21, 18, 21, 18)
        result_layout.addWidget(styled_label("RUN MANIFEST", "Kicker"))
        self.manifest_view = QLabel("아직 실행하지 않았습니다.")
        self.manifest_view.setObjectName("Manifest")
        self.manifest_view.setWordWrap(True)
        result_layout.addWidget(self.manifest_view, 1)
        content.addWidget(config, 1); content.addWidget(result, 2)
        layout.addLayout(content, 1)
        self.sim_log = QPlainTextEdit(); self.sim_log.setReadOnly(True); self.sim_log.setObjectName("Terminal")
        layout.addWidget(self.sim_log, 1)
        return page

    def build_future(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(section_title("FUTURE WORKFLOW PROTOTYPE", "앞으로 만들 기능을 먼저 만져봅니다", "화면과 입력 계약을 먼저 검증하며 Core 계산 결과로 사용하지 않습니다."))
        cards = QHBoxLayout()
        definitions = [
            ("A5", "Bottleneck Intelligence", "Flow share와 merge pressure 기반 가설 계약"),
            ("A6", "ROI Reduction", "상위 위험 Edge 중심 축소 모델 요청 계약"),
            ("A7", "Policy A/B Test", "동일 시드 기반 정책 비교 실험 계약"),
            ("DT", "Digital Twin Projection", "USD·Isaac Sim 투영 요청 계약"),
        ]
        for code, title, desc in definitions:
            frame = panel(); box = QVBoxLayout(frame); box.setContentsMargins(18, 17, 18, 17)
            code_label = QLabel(code); code_label.setObjectName("LabCode")
            name = QLabel(title); name.setObjectName("CardTitle")
            description = QLabel(desc); description.setObjectName("Muted"); description.setWordWrap(True)
            create = button("계약 생성", "secondary")
            create.clicked.connect(lambda checked=False, kind=code: self.create_future_contract(kind))
            box.addWidget(code_label); box.addWidget(name); box.addWidget(description); box.addStretch(1); box.addWidget(create)
            cards.addWidget(frame)
        layout.addLayout(cards, 1)
        self.future_output = QPlainTextEdit(); self.future_output.setReadOnly(True); self.future_output.setObjectName("Terminal")
        self.future_output.setPlaceholderText("생성된 프로토타입 계약이 여기에 표시됩니다.")
        layout.addWidget(self.future_output, 1)
        return page

    @staticmethod
    def make_table(headers: List[str]) -> QTableWidget:
        table = QTableWidget(0, len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)
        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        return table

    def switch_page(self, index: int) -> None:
        names = [
            ("워크스페이스", "물류 흐름을 한 화면에서 실험합니다"),
            ("입력 · CAD", "실제 모델 데이터를 연결합니다"),
            ("Flow 분석", "실제 Core 분석 결과를 확인합니다"),
            ("시뮬레이션", "결정론적 이벤트 실행을 제어합니다"),
            ("Future Lab", "다음 기능의 사용 경험을 먼저 검증합니다"),
        ]
        self.pages.setCurrentIndex(index)
        for position, nav in enumerate(self.nav_buttons):
            nav.setChecked(position == index)
        self.breadcrumb.setText(f"Sim_Core  /  {names[index][0]}")
        self.page_title.setText(names[index][1])

    def load_sample(self) -> None:
        root = sample_root()
        if not root:
            return
        self.facility_path = root / "facility.json"
        self.scenario_path = root / "scenario.json"
        candidate = root / "from_to.csv"
        self.demand_path = candidate if candidate.is_file() else None
        try:
            self.facility = read_json(self.facility_path)
            self.scenario = read_json(self.scenario_path)
            if hasattr(self, "file_cards"):
                self.file_cards["facility"].set_path(self.facility_path)
                self.file_cards["scenario"].set_path(self.scenario_path)
                self.file_cards["demand"].set_path(self.demand_path)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            QMessageBox.warning(self, "샘플 로드 실패", str(error))

    def select_file(self, key: str, value: str) -> None:
        path = Path(value)
        try:
            if key == "facility":
                self.facility_path = path
                self.facility = read_json(path)
                self.analysis = None
            elif key == "scenario":
                self.scenario_path = path
                self.scenario = read_json(path)
            elif key == "demand":
                self.demand_path = path
            elif key == "cad":
                self.cad_path = path
            self.refresh()
        except (OSError, ValueError, json.JSONDecodeError) as error:
            QMessageBox.critical(self, "파일 오류", str(error))

    def refresh(self) -> None:
        facility = self.facility or {}
        self.metric_nodes.set_value(len(facility.get("nodes", [])))
        self.metric_edges.set_value(len(facility.get("edges", [])))
        self.metric_stations.set_value(len(facility.get("stations", [])))
        self.metric_demands.set_value(demand_count(self.demand_path, self.scenario))
        self.network.set_model(self.facility, self.analysis)
        self.core_status.setText("●  Core 실행 가능" if self.core else "●  Core 미탑재")
        self.core_status.setProperty("ready", bool(self.core))
        self.core_status.style().unpolish(self.core_status)
        self.core_status.style().polish(self.core_status)
        self.core_path_label.setText(str(self.core) if self.core else "GitHub Actions에서 Windows EXE를 받으면 Core가 함께 포함됩니다.")
        scenario = self.scenario or {}
        self.sim_config.setText(
            f"Scenario\n  {scenario.get('scenario_id', '—')}\n\n"
            f"Duration\n  {float(scenario.get('duration_us', 0)) / 1_000_000:.3f} s\n\n"
            f"Vehicles\n  {len(scenario.get('vehicles', []))} 대\n\n"
            f"Jobs\n  {len(scenario.get('jobs', []))} 건\n\n"
            f"Master Seed\n  {scenario.get('master_seed', '—')}"
        )
        self.render_analysis()

    def run_core(self, action: str) -> None:
        if self.process.state() != QProcess.ProcessState.NotRunning:
            QMessageBox.information(self, "실행 중", "현재 Core 작업이 끝날 때까지 기다려 주세요.")
            return
        self.core = find_core()
        if not self.core:
            QMessageBox.warning(self, "Core 실행 파일 없음", "sim-core.exe를 찾지 못했습니다. GitHub Actions의 Windows 실행파일 패키지를 받거나 C++ Core를 먼저 빌드해 주세요.")
            return
        if action != "replay" and (not self.facility_path or not self.scenario_path):
            QMessageBox.warning(self, "입력 필요", "Facility JSON과 Scenario JSON을 먼저 선택해 주세요.")
            self.switch_page(1)
            return
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        run_dir = output_root() / stamp
        run_dir.mkdir(parents=True)
        arguments = [action, "--facility", str(self.facility_path), "--scenario", str(self.scenario_path)]
        self.current_output = None
        if action == "analyze":
            if self.demand_path:
                arguments += ["--from-to-csv", str(self.demand_path)]
            self.current_output = run_dir / "analysis-report.json"
            arguments += ["--output", str(self.current_output)]
            self.analysis_log.clear()
            self.analysis_log.appendPlainText(f"$ {self.core.name} {' '.join(arguments)}\n")
            self.switch_page(2)
        elif action == "run":
            self.current_output = run_dir / "simulation"
            arguments += ["--output", str(self.current_output)]
            self.sim_log.clear()
            self.sim_log.appendPlainText(f"$ {self.core.name} {' '.join(arguments)}\n")
            self.switch_page(3)
        else:
            self.analysis_log.clear()
            self.analysis_log.appendPlainText(f"$ {self.core.name} {' '.join(arguments)}\n")
            self.switch_page(2)
        self.current_action = action
        self.statusBar().showMessage(f"{action} 실행 중…")
        self.process.setWorkingDirectory(str(repository_root()))
        self.process.start(str(self.core), arguments)

    def capture_stdout(self) -> None:
        text = bytes(self.process.readAllStandardOutput()).decode("utf-8", errors="replace")
        target = self.sim_log if self.current_action == "run" else self.analysis_log
        target.moveCursor(QTextCursor.End)
        target.insertPlainText(text)

    def capture_stderr(self) -> None:
        text = bytes(self.process.readAllStandardError()).decode("utf-8", errors="replace")
        target = self.sim_log if self.current_action == "run" else self.analysis_log
        target.moveCursor(QTextCursor.End)
        target.insertPlainText("\n[stderr]\n" + text)

    def process_finished(self, exit_code: int, _status: QProcess.ExitStatus) -> None:
        self.statusBar().showMessage(f"{self.current_action} 완료 · exit {exit_code}", 8000)
        try:
            if self.current_action == "analyze" and self.current_output and self.current_output.is_file():
                self.analysis = read_json(self.current_output)
                self.refresh()
            elif self.current_action == "run" and self.current_output:
                manifest = self.current_output / "run_manifest.json"
                if manifest.is_file():
                    self.last_manifest = read_json(manifest)
                    self.render_manifest()
        except (OSError, ValueError, json.JSONDecodeError) as error:
            QMessageBox.warning(self, "결과 해석 실패", str(error))
        if exit_code != 0:
            QMessageBox.warning(self, "Core 실행 결과", f"종료 코드 {exit_code}입니다. 화면 하단 로그를 확인해 주세요.")

    def render_analysis(self) -> None:
        report = self.analysis or {}
        edge_flows = report.get("edge_flows", [])
        node_flows = report.get("node_flows", [])
        station_flows = report.get("station_flows", [])
        diagnostics = report.get("diagnostics", [])
        errors = sum(1 for item in diagnostics if str(item.get("severity", "")).lower() == "error")
        self.analysis_status_card.set_value("PASS" if report and not errors else ("FAIL" if report else "—"))
        self.route_card.set_value(len(report.get("demand_routes", [])) if report else "—")
        self.top_flow_card.set_value(f"{max([float(item.get('expected_moves_per_hour', 0)) for item in edge_flows] or [0]):.1f}" if report else "—")
        self.merge_card.set_value(f"{max([float(item.get('merge_pressure', 0)) for item in node_flows] or [0]):.1f}" if report else "—")
        self.edge_table.setRowCount(len(edge_flows))
        for row, item in enumerate(sorted(edge_flows, key=lambda value: float(value.get("expected_moves_per_hour", 0)), reverse=True)):
            values = [item.get("edge_id"), f"{float(item.get('expected_moves_per_hour', 0)):.2f}", f"{float(item.get('flow_share', 0)) * 100:.1f}%", item.get("demand_count")]
            for column, value in enumerate(values): self.edge_table.setItem(row, column, QTableWidgetItem(str(value)))
        self.station_table.setRowCount(len(station_flows))
        for row, item in enumerate(sorted(station_flows, key=lambda value: float(value.get("utilization_ratio", 0)), reverse=True)):
            values = [item.get("station_id"), f"{float(item.get('peak_moves_per_hour', 0)):.2f}", f"{float(item.get('utilization_ratio', 0)) * 100:.1f}%", f"{float(item.get('capacity_margin_per_hour', 0)):.2f}"]
            for column, value in enumerate(values): self.station_table.setItem(row, column, QTableWidgetItem(str(value)))

    def render_manifest(self) -> None:
        manifest = self.last_manifest or {}
        self.manifest_view.setText(
            f"Status\n  {manifest.get('status', '—')}\n\n"
            f"Processed Events\n  {manifest.get('processed_event_count', '—')}\n\n"
            f"Final Time\n  {float(manifest.get('final_simulation_time_us', 0)) / 1_000_000:.3f} s\n\n"
            f"Trace Hash\n  {manifest.get('trace_hash', '—')}\n\n"
            f"Run Fingerprint\n  {manifest.get('run_fingerprint', '—')}"
        )

    def save_cad_contract(self) -> None:
        if not self.cad_path:
            QMessageBox.warning(self, "CAD 파일 필요", "CAD 원본을 먼저 선택해 주세요.")
            return
        contract = {
            "schema_version": "0.1.0-prototype",
            "contract_type": "cad-import-request",
            "implementation_status": "ADAPTER_NOT_CONNECTED",
            "source": {"file_name": self.cad_path.name, "extension": self.cad_path.suffix.lower(), "size_bytes": self.cad_path.stat().st_size},
            "coordinate": {"source_unit": self.cad_unit.currentText(), "up_axis": "Z", "target_frame": "local-fab"},
            "mapping": {"rail_center_layer": self.rail_layer.text(), "station_layer": self.station_layer.text(), "direction_layer": self.direction_layer.text()},
        }
        path, _ = QFileDialog.getSaveFileName(self, "CAD Import 계약 저장", "cad-import-contract.json", "JSON (*.json)")
        if path:
            Path(path).write_text(json.dumps(contract, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def create_future_contract(self, kind: str) -> None:
        names = {"A5": "bottleneck-preview", "A6": "roi-reduction-request", "A7": "policy-ab-request", "DT": "digital-twin-projection-request"}
        contract = {
            "schema_version": "0.1.0-prototype",
            "contract_type": names[kind],
            "implementation_status": "CORE_NOT_CONNECTED",
            "authoritative": False,
            "model_revision_id": (self.facility or {}).get("revision_id"),
            "scenario_id": (self.scenario or {}).get("scenario_id"),
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
        self.future_output.setPlainText(json.dumps(contract, ensure_ascii=False, indent=2))


STYLESHEET = """
* { font-family: "Segoe UI", "Malgun Gothic"; font-size: 12px; color: #e8f3f7; }
QMainWindow, #Body { background: #071019; }
#Sidebar { background: #050d15; border-right: 1px solid #172834; }
#Brand { color: #43e4d3; font-size: 16px; font-weight: 700; line-height: 1.4; }
#NavButton { text-align: left; border: 0; border-radius: 10px; padding: 12px 13px; color: #8fa5b4; background: transparent; min-height: 22px; }
#NavButton:hover { color: #edf7fb; background: #0d1c28; }
#NavButton:checked { color: #eafffb; background: #0e2b32; border-left: 3px solid #43e4d3; }
#CoreCard { background: #0b1b27; border: 1px solid #1b3442; border-radius: 11px; }
#CoreStatus { color: #ffb86b; font-weight: 700; }
#CoreStatus[ready="true"] { color: #6ee7a5; }
#TinyMuted, #SidebarFooter { color: #5f7886; font-size: 9px; }
#SidebarFooter { padding-top: 10px; }
#Breadcrumb { color: #607987; font-size: 10px; }
#PageTitle { color: #edf7fb; font-size: 23px; font-weight: 650; }
#Panel, #MetricCard, #FileCard { background: #0d1b28; border: 1px solid #1b3240; border-radius: 15px; }
#FileCard[prototype="true"] { border-top: 2px solid #806fd0; }
#Kicker { color: #43e4d3; font-size: 9px; font-weight: 800; letter-spacing: 2px; }
#SectionTitle { font-size: 23px; font-weight: 700; }
#HeroTitle { font-size: 28px; font-weight: 700; line-height: 1.25; }
#Muted { color: #8ca3b3; font-size: 10px; }
#Orbit { background: #0a202b; border: 4px solid #2cc7c2; border-radius: 75px; }
#MetricLabel { color: #8ca3b3; font-size: 9px; font-weight: 700; }
#MetricValue { font-size: 24px; font-weight: 700; }
#MetricSub { color: #607987; font-size: 9px; }
#MetricIcon { color: #43e4d3; font-size: 18px; }
#FileIcon { color: #43e4d3; font-size: 25px; background: #0b2a31; border: 1px solid #16434a; border-radius: 14px; padding: 12px; }
#CardTitle { font-size: 14px; font-weight: 700; }
#FileName { color: #607987; font-size: 9px; }
#AvailableBadge, #PrototypeBadge { font-size: 8px; font-weight: 700; padding: 3px 7px; border-radius: 8px; }
#AvailableBadge { color: #6ee7a5; background: #102c24; border: 1px solid #20503c; }
#PrototypeBadge { color: #bba8ff; background: #251f3d; border: 1px solid #44386a; }
QPushButton { border: 1px solid #294452; border-radius: 9px; padding: 8px 14px; background: #112735; font-weight: 650; }
QPushButton:hover { border-color: #43e4d3; background: #153241; }
QPushButton[kind="primary"] { color: #021311; background: #43e4d3; border-color: #5af1e1; }
QPushButton[kind="primary"]:hover { background: #62eee0; }
QLineEdit, QComboBox { background: #07151f; border: 1px solid #294452; border-radius: 8px; padding: 8px; min-height: 20px; }
QLineEdit:focus, QComboBox:focus { border-color: #43e4d3; }
#FieldLabel { color: #8ca3b3; font-size: 9px; }
#NetworkView { border-radius: 10px; background: #07131d; }
QTableWidget { background: #091722; alternate-background-color: #0c1d29; border: 0; gridline-color: #1b3240; selection-background-color: #16454d; }
QHeaderView::section { background: #0c202d; color: #78909d; border: 0; border-bottom: 1px solid #25404d; padding: 8px; font-size: 9px; }
#Terminal { background: #040d14; border: 1px solid #1b3240; border-radius: 11px; color: #a9c8d2; font-family: Consolas; font-size: 10px; padding: 10px; }
#Definition, #Manifest { color: #b7cbd4; font-family: Consolas; font-size: 11px; padding: 12px; }
#LabCode { color: #bba8ff; background: #211c35; border: 1px solid #44386a; border-radius: 12px; padding: 10px; font-size: 15px; font-weight: 800; max-width: 32px; }
QStatusBar { background: #050d15; color: #78909d; border-top: 1px solid #172834; }
QScrollBar:vertical { background: #071019; width: 9px; }
QScrollBar::handle:vertical { background: #284452; border-radius: 4px; min-height: 25px; }
"""


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Sim_Core Flow Workbench")
    app.setOrganizationName("Mega-Sim")
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
