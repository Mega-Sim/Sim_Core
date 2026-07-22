"""Compatibility launcher that applies graph UI enhancements to the existing app."""
from __future__ import annotations

import app as _app
from graph_ui_enhancer import install_enhancements

install_enhancements(_app)

MainWindow = _app.MainWindow
main = _app.main

if __name__ == "__main__":
    raise SystemExit(main())
