"""NVIDIA Isaac Sim modeling page integration for the English Sim_Core desktop workbench."""
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


def _contains_hangul(value: str) -> bool:
    return any("가" <= character <= "힣" for character in value)


def _english_error(error: Exception, fallback: str) -> str:
    text = str(error).strip()
    return fallback if not text or _contains_hangul(text) else text


def _normalize_layout_messages(layout: dict[str, Any]) -> dict[str, Any]:
    validation = layout.get("validation")
    if not isinstance(validation, dict):
        return layout
    warnings = validation.get("warnings")
    if isinstance(warnings, list):
        validation["warnings"] = [
            "No station labels were found in the Graph metadata."
            if _contains_hangul(str(warning))
            else str(warning)
            for warning in warnings
        ]
    errors = validation.get("errors")
    if isinstance(errors, list):
        validation["errors"] = [
            "The source layout contains validation errors."
            if _contains_hangul(str(error))
            else str(error)
            for error in errors
        ]
    return layout


def install_isaac_sim_modeling(base_module: Any) -> None:
    """Add a Graph/AutoMod to Isaac Sim modeling workflow as a separate page."""

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
        self.page_title.setText("Convert Graph and AutoMod layouts into an Isaac Sim Stage")

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
                "Isaac Sim Modeling · Rough Pipeline",
                "Reuse the AutoMod_Isaacsim pm.asy-to-meter directional Layout JSON structure "
                "to convert the current Sim_Core CAD Graph or an AutoMod pm.asy file into a USDA Stage that can be opened directly in Isaac Sim.",
            )
        )

        source_panel = base_module.panel()
        source_layout = QVBoxLayout(source_panel)
        source_layout.setContentsMargins(22, 19, 22, 19)
        source_layout.setSpacing(12)
        source_layout.addWidget(
            base_module.section_title(
                "01 · SOURCE",
                "Select Model Source",
                "Use the current CAD Graph or load a pm.asy file from an existing AutoMod model.arc directory.",
            )
        )
        source_buttons = QHBoxLayout()
        use_graph = base_module.button("Use Current CAD Graph", "primary")
        use_graph.clicked.connect(self.use_current_graph_for_isaac)
        choose_pm = base_module.button("Select AutoMod pm.asy", "secondary")
        choose_pm.clicked.connect(self.select_automod_pm_for_isaac)
        source_buttons.addWidget(use_graph)
        source_buttons.addWidget(choose_pm)
        source_buttons.addStretch(1)
        source_layout.addLayout(source_buttons)
        self.isaac_source_status = QLabel("No source selected · Select a CAD Graph or pm.asy file.")
        self.isaac_source_status.setObjectName("Muted")
        self.isaac_source_status.setWordWrap(True)
        source_layout.addWidget(self.isaac_source_status)
        layout.addWidget(source_panel)

        flow = QHBoxLayout()
        for code, title, description in [
            ("1", "Layout JSON", "Normalize coordinates to meters and separate directed Guide Paths, Stations, and Routing Points."),
            ("2", "USD Stage", "Generate isaac_stage.usda with Guide Paths as BasisCurves and Stations as placeholder Cubes."),
            ("3", "Isaac Loader", "Generate load_in_isaac_sim.py for opening the Stage from the Isaac Sim Script Editor."),
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
                "Generate Isaac Sim Model Package",
                "This is a rough modeling pipeline. It currently generates rail and station placement; OHT/AMR 3D assets and physical properties can be added in later phases.",
            )
        )
        export_row = QHBoxLayout()
        self.isaac_export_button = base_module.button("Generate Isaac Sim Model", "primary")
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
            "Select a source to display Node, Edge, Station counts and conversion status."
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
                "CAD Graph Required",
                "Convert a DXF or Rail file into a Graph from the Input · CAD menu first.",
            )
            return
        try:
            self.isaac_layout = _normalize_layout_messages(build_isaac_layout_from_graph(graph))
        except IsaacSimExportError as error:
            QMessageBox.critical(
                self,
                "Isaac Conversion Failed",
                _english_error(
                    error,
                    "The current CAD Graph could not be converted. Check Nodes, Edges, and explicit edge directions.",
                ),
            )
            return
        self.isaac_source_path = getattr(self, "cad_path", None)
        label = (
            f"Current CAD Graph · {self.isaac_source_path.name}"
            if self.isaac_source_path
            else "Current CAD Graph"
        )
        self.isaac_source_status.setText(f"Selected · {label}")
        self.update_isaac_summary(label)
        self.statusBar().showMessage("The current CAD Graph is connected as the Isaac Sim modeling source.", 6000)

    def select_automod_pm_for_isaac(self: Any) -> None:
        default_dir = str(
            Path(getattr(self, "cad_path", Path.home())).parent
            if getattr(self, "cad_path", None)
            else Path.home()
        )
        selected, _ = QFileDialog.getOpenFileName(
            self,
            "Select AutoMod pm.asy",
            default_dir,
            "AutoMod movement system (pm.asy);;ASY files (*.asy);;All files (*)",
        )
        if not selected:
            return
        source = Path(selected)
        try:
            self.isaac_layout = _normalize_layout_messages(load_automod_pm_layout(source))
        except (IsaacSimExportError, OSError) as error:
            QMessageBox.critical(
                self,
                "pm.asy Conversion Failed",
                _english_error(error, "The selected AutoMod pm.asy file could not be converted."),
            )
            return
        self.isaac_source_path = source
        label = f"AutoMod pm.asy · {source}"
        self.isaac_source_status.setText(f"Selected · {label}")
        self.update_isaac_summary(label)
        self.statusBar().showMessage("The AutoMod pm.asy file was converted into an Isaac Sim modeling source.", 6000)

    def export_isaac_sim_package(self: Any) -> None:
        if not self.isaac_layout:
            QMessageBox.warning(self, "Model Source Required", "Select a CAD Graph or AutoMod pm.asy file first.")
            return
        source = self.isaac_source_path
        default_dir = source.parent if isinstance(source, Path) else Path.home() / "Documents"
        selected = QFileDialog.getExistingDirectory(
            self,
            "Select Parent Folder for Isaac Sim Model Output",
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
            QMessageBox.critical(
                self,
                "Isaac Model Generation Failed",
                _english_error(error, "The Isaac Sim model package could not be generated."),
            )
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
        self.statusBar().showMessage(f"Isaac Sim model generation completed · {target}", 10000)
        QMessageBox.information(
            self,
            "Isaac Sim Model Generation Completed",
            f"{target}\n\nOpen isaac_stage.usda in Isaac Sim or run "
            "load_in_isaac_sim.py from the Script Editor.",
        )

    cls.build_sidebar = build_sidebar
    cls.build_ui = build_ui
    cls.switch_page = switch_page
    cls.build_isaac_sim_modeling = build_isaac_sim_modeling
    cls.update_isaac_summary = update_isaac_summary
    cls.use_current_graph_for_isaac = use_current_graph_for_isaac
    cls.select_automod_pm_for_isaac = select_automod_pm_for_isaac
    cls.export_isaac_sim_package = export_isaac_sim_package
