"""Keep SemiLA .rail loading available after Layout static-analysis integration."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMessageBox

from rail_file import RailFileError, load_rail_graph


def install_rail_compat(base_module: Any) -> None:
    """Add .rail selection/loading without replacing Random/Actual FromTo logic."""

    cls = base_module.MainWindow
    if getattr(cls, "_rail_compat_installed", False):
        return
    cls._rail_compat_installed = True

    original_build_inputs = cls.build_inputs
    original_convert = cls.convert_cad_graph

    def build_inputs(self: Any) -> Any:
        page = original_build_inputs(self)
        card = getattr(self, "file_cards", {}).get("cad")
        if card is not None:
            card.file_filter = "Rail / DXF (*.rail *.dxf)"
        return page

    def convert_cad_graph(self: Any) -> None:
        cad_path = getattr(self, "cad_path", None)
        if not cad_path or Path(cad_path).suffix.casefold() != ".rail":
            original_convert(self)
            return

        path = Path(cad_path)
        status = getattr(self, "cad_graph_status", None)
        save_button = getattr(self, "cad_save_button", None)
        if status is not None:
            status.setText("Rail geometry를 경량 Rail Graph로 불러오는 중입니다…")
        if save_button is not None:
            save_button.setEnabled(False)
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        QApplication.processEvents()
        try:
            graph = load_rail_graph(path)
        except (RailFileError, OSError) as error:
            self.cad_graph = None
            self.cad_graph_path = None
            self.cad_graph_view.set_graph(None)
            if status is not None:
                status.setText(f"Rail 변환 실패\n{error}")
            QMessageBox.critical(self, "Rail 변환 실패", str(error))
            return
        finally:
            QApplication.restoreOverrideCursor()

        self.cad_graph = graph
        self.cad_graph_path = None
        self.cad_graph_view.set_graph(graph)
        if save_button is not None:
            save_button.setEnabled(True)
        metadata = graph.get("metadata", {})
        statistics = metadata.get("statistics", {})
        if status is not None:
            status.setText(
                f"{int(statistics.get('node_count', 0)):,} Nodes  ·  "
                f"{int(statistics.get('edge_count', 0)):,} Edges\n"
                "Source Rail  ·  경량 Rail 준비 완료  ·  저장 전"
            )
        graph_changed = getattr(self, "_bind_current_cad_graph", None)
        if callable(graph_changed):
            graph_changed(clear_outputs=True)
        self.statusBar().showMessage(
            f"Rail Graph 변환 완료 · {int(statistics.get('node_count', 0)):,} nodes / "
            f"{int(statistics.get('edge_count', 0)):,} edges",
            8000,
        )
        self.refresh()

    cls.build_inputs = build_inputs
    cls.convert_cad_graph = convert_cad_graph
