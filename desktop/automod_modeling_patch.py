"""AutoMod model conversion UI integration for the current desktop workbench."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from PySide6.QtWidgets import QFileDialog, QMessageBox

from automod_pm_converter import AutoModConversionError, save_automod_model


def install_automod_modeling(base_module: Any) -> None:
    """Add AutoMod model.arc export without replacing current Graph/Layout features."""

    cls = base_module.MainWindow
    if getattr(cls, "_automod_modeling_installed", False):
        return
    cls._automod_modeling_installed = True

    original_build_inputs = cls.build_inputs
    original_convert_cad_graph = cls.convert_cad_graph

    def build_inputs(self: Any) -> Any:
        page = original_build_inputs(self)
        self.cad_automod_path = None
        panel = self.cad_save_button.parentWidget()
        form = panel.layout()
        self.cad_automod_button = base_module.button("AutoMod 모델변환", "primary")
        self.cad_automod_button.setEnabled(bool(getattr(self, "cad_graph", None)))
        self.cad_automod_button.clicked.connect(self.save_automod_model)
        # Keep the existing Rail/DXF conversion and Graph JSON controls in place.
        form.addWidget(self.cad_automod_button, 4, 3)
        return page

    def convert_cad_graph(self: Any) -> None:
        original_convert_cad_graph(self)
        if hasattr(self, "cad_automod_button"):
            self.cad_automod_button.setEnabled(bool(getattr(self, "cad_graph", None)))
        if not getattr(self, "cad_graph", None):
            self.cad_automod_path = None

    def save_model(self: Any) -> None:
        if not getattr(self, "cad_graph", None) or not getattr(self, "cad_path", None):
            QMessageBox.warning(self, "변환 결과 필요", "CAD/Rail Graph를 먼저 변환해 주세요.")
            return
        parent = QFileDialog.getExistingDirectory(
            self,
            "model.arc를 생성할 상위 폴더 선택",
            str(Path(self.cad_path).parent),
        )
        if not parent:
            return
        target = Path(parent) / "model.arc"
        try:
            generated = save_automod_model(self.cad_graph, target)
            self.cad_automod_path = generated.archive
        except (AutoModConversionError, OSError) as error:
            QMessageBox.critical(self, "AutoMod 변환 실패", str(error))
            return

        statistics = self.cad_graph.get("metadata", {}).get("statistics", {})
        self.cad_graph_status.setText(
            f"{int(statistics.get('node_count', 0)):,} Nodes  ·  "
            f"{int(statistics.get('edge_count', 0)):,} Edges\n"
            f"AutoMod 변환 완료 · {self.cad_automod_path.name}/pm.asy"
        )
        self.statusBar().showMessage(
            f"AutoMod model.arc 변환 완료 · {self.cad_automod_path}", 8000
        )

    cls.build_inputs = build_inputs
    cls.convert_cad_graph = convert_cad_graph
    cls.save_automod_model = save_model
