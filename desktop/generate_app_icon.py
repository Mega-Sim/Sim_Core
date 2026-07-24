"""Generate the Windows executable icon for the English Sim_Core workbench build."""
from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QGuiApplication, QImage, QPainter, QPainterPath, QPen


def draw_icon(size: int = 512) -> QImage:
    image = QImage(size, size, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)
    painter = QPainter(image)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    scale = size / 256.0

    def p(value: float) -> float:
        return value * scale

    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(QColor("#071621"))
    painter.drawRoundedRect(QRectF(p(12), p(12), p(232), p(232)), p(52), p(52))

    painter.setPen(QPen(QColor(58, 104, 125, 110), p(2)))
    for offset in (64, 96, 128, 160, 192):
        painter.drawLine(QPointF(p(offset), p(36)), QPointF(p(offset), p(220)))
        painter.drawLine(QPointF(p(36), p(offset)), QPointF(p(220), p(offset)))

    path = QPainterPath(QPointF(p(48), p(174)))
    path.cubicTo(QPointF(p(88), p(174)), QPointF(p(82), p(92)), QPointF(p(126), p(92)))
    path.cubicTo(QPointF(p(166), p(92)), QPointF(p(158), p(154)), QPointF(p(210), p(154)))
    painter.setPen(QPen(QColor("#49E6D3"), p(15), Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    painter.setBrush(Qt.BrushStyle.NoBrush)
    painter.drawPath(path)

    painter.setPen(QPen(QColor("#D9FFFF"), p(4)))
    painter.setBrush(QColor("#0A3440"))
    for x, y in ((48, 174), (126, 92), (210, 154)):
        painter.drawEllipse(QPointF(p(x), p(y)), p(14), p(14))

    painter.setPen(QPen(QColor("#8AB8FF"), p(6), Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    painter.setBrush(QColor(16, 39, 66, 220))
    cube = QPainterPath(QPointF(p(98), p(50)))
    cube.lineTo(QPointF(p(128), p(34)))
    cube.lineTo(QPointF(p(158), p(50)))
    cube.lineTo(QPointF(p(128), p(67)))
    cube.closeSubpath()
    painter.drawPath(cube)
    painter.drawLine(QPointF(p(98), p(50)), QPointF(p(98), p(78)))
    painter.drawLine(QPointF(p(158), p(50)), QPointF(p(158), p(78)))
    painter.drawLine(QPointF(p(98), p(78)), QPointF(p(128), p(95)))
    painter.drawLine(QPointF(p(158), p(78)), QPointF(p(128), p(95)))
    painter.drawLine(QPointF(p(128), p(67)), QPointF(p(128), p(95)))

    painter.end()
    return image


def main() -> int:
    app = QGuiApplication(sys.argv)
    output = Path(__file__).resolve().parent / "generated" / "sim_core_workbench.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    image = draw_icon()
    if not image.save(str(output), "PNG"):
        raise RuntimeError(f"Failed to save application icon: {output}")
    print(output)
    app.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
