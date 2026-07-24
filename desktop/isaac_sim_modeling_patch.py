"""NVIDIA Isaac Sim modeling page integration for the Sim_Core desktop workbench."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from isaac_sim_exporter import (
    IsaacSimExportError,
    build_isaac_layout_from_graph,
    load_automod_pm_layout,
    save_isaac_package,
)


ISAAC_PAGE_INDEX = 5


def install_isaac_sim_modeling(base_module: Any) -> None:
    """Add a rough Graph/AutoMod -> Isaac Sim modeling workflow as a separate page."""

    cls = base_module.MainWindow
    if getattr(cls, "_isaac_sim_modeling_installed", False):
        return
    cls._isaac_sim_modeling_installed = True

    original_build_sidebar = cls.build_sidebar
    original_build_ui = cls.build_ui
    original_switch_page = cls.switch_page

    def build_sidebar(self: Any) -> QWidget:
        side = original_build_sidebar(self)
        layout = side.layout()
        insert_index = 2 + len(self.nav_buttons)
        nav = QPushButton("◈   NVIDIA Isaac Sim Modeling")
        nav.setObjectName("NavButton")
        nav.setCheckable(True)
        nav.setCursor(Qt.PointingHandCursor)
        nav.clicked.connect(lambda checked=False: self.switch_page(ISAAC_PAGE_INDEX))
        layout.insertWidget(insert_index, nav)
        self.nav_buttons.append(nav)
        return side

    def build_ui(self: Any) -> None:
        original_build_ui(self)
        self.pages.addWidget(self.build_isaac_sim_modeling())

    def switch_page(self: Any, index: int) -> None:
        if index != ISAAC_PAGE_INDEX:
            original_switch_page(self, index)
            return
        self.pages.setCurrentIndex(index)
        for position, nav in enumerate(self.nav_buttons):
            nav.setChecked(position == index)
        self.breadcrumb.setText("Sim_Core  /  NVIDIA Isaac Sim Modeling")
        self.page_title.setText("Graph와 AutoMod 레이아웃을 Isaac Sim Stage로 변환합니다")

    def build_isaac_sim_modeling(self: Any) -> QWidget:
        self.isaac_layout = None
        self.isaac_source_path = None
        self.isaac_output_dir = None

        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)
        layout.addWidget(
            base_module.section_title(
                "NVIDIA ISAAC SIM MODELING",
                "Isaac Sim 모델링 · Rough Pipeline",
                "AutoMod_Isaacsim의 pm.asy → 미터 단위 방향성 Layout JSON 구조를 가져와 "
                "현재 Sim_Core CAD Graph 또는 AutoMod pm.asy를 Isaac Sim에서 바로 열 수 있는 USDA Stage로 변환합니다.",
            )
        )

        source_panel = base_module.panel()
        source_layout = QVBoxLayout(source_panel)
        source_layout.setContentsMargins(22, 19, 22, 19)
        source_layout.setSpacing(12)
        source_layout.addWidget(
            base_module.section_title(
                "01 · SOURCE",
                "모델 소스 선택",
                "현재 작업 중인 CAD Graph를 그대로 사용하거나 기존 AutoMod model.arc의 pm.asy를 불러올 수 있습니다.",
            )
        )
        source_buttons = QHBoxLayout()
        use_graph = base_module.button("현재 CAD Graph 사용", "primary")
        use_graph.clicked.connect(self.use_current_graph_for_isaac)
        choose_pm = base_module.button("AutoMod pm.asy 선택", "secondary")
        choose_pm.clicked.connect(self.select_automod_pm_for_isaac)
        source_buttons.addWidget(use_graph)
        source_buttons.addWidget(choose_pm)
        source_buttons.addStretch(1)
        source_layout.addLayout(source_buttons)
        self.isaac_source_status = QLabel("소스 미선택 · CAD Graph 또는 pm.asy를 선택해 주세요.")
        self.isaac_source_status.setObjectName("Muted")
        self.isaac_source_status.setWordWrap(True)
        source_layout.addWidget(self.isaac_source_status)
        layout.addWidget(source_panel)

        flow = QHBoxLayout()
        for code, title, description in [
            ("1", "Layout JSON", "좌표를 meter로 정규화하고 방향성 Guide Path, Station, Routing Point를 분리합니다."),
            ("2", "USD Stage", "Guide Path는 BasisCurves, Station은 placeholder Cube로 구성한 isaac_stage.usda를 생성합니다."),
            ("3", "Isaac Loader", "Isaac Sim Script Editor에서 Stage를 여는 load_in_isaac_sim.py를 함께 생성합니다."),
        ]:
            card = QFrame()
            card.setObjectName("Panel")
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(18, 16, 18, 16)
            badge = QLabel(code)
            badge.setObjectName("Kicker")
            heading = QLabel(title)
            heading.setObjectName("CardTitle")
            desc = QLabel(description)
            desc.setObjectName("Muted")
            desc.setWordWrap(True)
            card_layout.addWidget(badge)
            card_layout.addWidget(heading)
            card_layout.addWidget(desc)
            card_layout.addStretch(1)
            flow.addWidget(card)
        layout.addLayout(flow)

        output_panel = base_module.panel()
        output_layout = QVBoxLayout(output_panel)
        output_layout.setContentsMargins(22, 19, 22, 19)
        output_layout.setSpacing(10)
        output_layout.addWidget(
            base_module.section_title(
                "02 · EXPORT",
                "Isaac Sim 모델 패키지 생성",
                "현재 단계는 러프 모델링용입니다. 레일/스테이션 배치까지 생성하고 OHT·AMR 3D Asset 연결과 물리 속성은 다음 단계에서 확장합니다.",
            )
        )
        export_row = QHBoxLayout()
        self.isaac_export_button = base_module.button("Isaac Sim 모델 생성", "primary")
        self.isaac_export_button.setEnabled(False)
        self.isaac_export_button.clicked.connect(self.export_isaac_sim_package)
        export_row.addWidget(self.isaac_export_button)
        export_row.addStretch(1)
        output_layout.addLayout(export_row)
        self.isaac_summary = QPlainTextEdit()
        self.isaac_summary.setReadOnly(True)
        self.isaac_summary.setObjectName("Terminal")
        self.isaac_summary.setMinimumHeight(165)
        self.isaac_summary.setPlaceholderText(
            "소스를 선택하면 Node / Edge / Station 수와 변환 상태가 표시됩니다."
        )
        output_layout.addWidget(self.isaac_summary)
        layout.addWidget(output_panel, 1)
        return page

    def update_isaac_summary(self: Any, source_label: str) -> None:
        layout = self.isaac_layout or {}
        summary = layout.get("validation", {}).get("summary", {})
        warnings = layout.get("validation", {}).get("warnings", [])
        station_count = int(summary.get("station_count", len(layout.get("stations", []))))
        text = [
            f"Source      : {source_label}",
            f"Nodes       : {int(summary.get('node_count', len(layout.get('nodes', [])))):,}",
            f"Edges       : {int(summary.get('edge_count', len(layout.get('edges', [])))):,}",
            f"Stations    : {station_count:,}",
            f"Routing CPs : {len(layout.get('routing_control_points', [])):,}",
            "",
            "Output",
            "  - isaac_layout.json",
            "  - isaac_stage.usda",
            "  - load_in_isaac_sim.py",
            "  - isaac_manifest.json",
        ]
        if warnings:
            text.extend(["", "Warnings"])
            text.extend(f"  - {warning}" for warning in warnings[:8])
        self.isaac_summary.setPlainText("\n".join(text))
        self.isaac_export_button.setEnabled(True)

    def use_current_graph_for_isaac(self: Any) -> None:
        graph = getattr(self, "cad_graph", None)
        if not graph:
            QMessageBox.warning(
                self,
                "CAD Graph 필요",
                "입력 · CAD 메뉴에서 DXF/Rail을 먼저 Graph로 변환해 주세요.",
            )
            return
        try:
            self.isaac_layout = build_isaac_layout_from_graph(graph)
        except IsaacSimExportError as error:
            QMessageBox.critical(self, "Isaac 변환 실패", str(error))
            return
        self.isaac_source_path = getattr(self, "cad_path", None)
        label = (
            f"현재 CAD Graph · {self.isaac_source_path.name}"
            if self.isaac_source_path
            else "현재 CAD Graph"
        )
        self.isaac_source_status.setText(f"선택 완료 · {label}")
        self.update_isaac_summary(label)
        self.statusBar().showMessage("현재 CAD Graph를 Isaac Sim 모델링 소스로 연결했습니다.", 6000)

    def select_automod_pm_for_isaac(self: Any) -> None:
        default_dir = str(
            Path(getattr(self, "cad_path", Path.home())).parent
            if getattr(self, "cad_path", None)
            else Path.home()
        )
        selected, _ = QFileDialog.getOpenFileName(
            self,
            "AutoMod pm.asy 선택",
            default_dir,
            "AutoMod movement system (pm.asy);;ASY files (*.asy);;All files (*)",
        )
        if not selected:
            return
        source = Path(selected)
        try:
            self.isaac_layout = load_automod_pm_layout(source)
        except (IsaacSimExportError, OSError) as error:
            QMessageBox.critical(self, "pm.asy 변환 실패", str(error))
            return
        self.isaac_source_path = source
        label = f"AutoMod pm.asy · {source}"
        self.isaac_source_status.setText(f"선택 완료 · {label}")
        self.update_isaac_summary(label)
        self.statusBar().showMessage("AutoMod pm.asy를 Isaac Sim 모델링 소스로 변환했습니다.", 6000)

    def export_isaac_sim_package(self: Any) -> None:
        if not self.isaac_layout:
            QMessageBox.warning(self, "모델 소스 필요", "CAD Graph 또는 AutoMod pm.asy를 먼저 선택해 주세요.")
            return
        source = self.isaac_source_path
        default_dir = source.parent if isinstance(source, Path) else Path.home() / "Documents"
        selected = QFileDialog.getExistingDirectory(
            self,
            "Isaac Sim 모델 출력 상위 폴더 선택",
            str(default_dir),
        )
        if not selected:
            return
        stem = source.stem if isinstance(source, Path) else "Sim_Core_Model"
        if stem.casefold() == "pm":
            stem = source.parent.parent.name if source.parent.name.casefold() == "model.arc" else "AutoMod_Model"
        target = Path(selected) / f"{stem}_IsaacSim"
        try:
            generated = save_isaac_package(self.isaac_layout, target)
        except (IsaacSimExportError, OSError, ValueError) as error:
            QMessageBox.critical(self, "Isaac 모델 생성 실패", str(error))
            return
        self.isaac_output_dir = target
        current = self.isaac_summary.toPlainText()
        self.isaac_summary.setPlainText(
            current
            + "\n\nGenerated\n"
            + f"  Layout : {generated['layout']}\n"
            + f"  Stage  : {generated['stage']}\n"
            + f"  Loader : {generated['loader']}\n"
        )
        self.statusBar().showMessage(f"Isaac Sim 모델 생성 완료 · {target}", 10000)
        QMessageBox.information(
            self,
            "Isaac Sim 모델 생성 완료",
            f"{target}\n\nIsaac Sim에서 isaac_stage.usda를 열거나 "
            "Script Editor에서 load_in_isaac_sim.py를 실행해 주세요.",
        )

    cls.build_sidebar = build_sidebar
    cls.build_ui = build_ui
    cls.switch_page = switch_page
    cls.build_isaac_sim_modeling = build_isaac_sim_modeling
    cls.update_isaac_summary = update_isaac_summary
    cls.use_current_graph_for_isaac = use_current_graph_for_isaac
    cls.select_automod_pm_for_isaac = select_automod_pm_for_isaac
    cls.export_isaac_sim_package = export_isaac_sim_package
