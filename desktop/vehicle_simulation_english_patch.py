"""English translation fragments for the 2D Vehicle Simulation workflow."""
from __future__ import annotations

from typing import Any

import english_ui_patch


_TRANSLATIONS = [
    (
        "랜덤 FromTo 생성 후 실행할 수 있습니다. Pickup/Setdown 이적재 시간은 각각 10초입니다.",
        "Generate Random FromTo first. Pickup and setdown service each take 10 seconds.",
    ),
    (
        "2D Vehicle Simulation은 먼저 랜덤 FromTo 모드에서 생성한 Job으로 실행합니다.",
        "2D Vehicle Simulation runs with Jobs generated in Random FromTo mode.",
    ),
    (
        "현재 Layout에서 랜덤 FromTo 정적분석을 먼저 실행해 주세요.",
        "Run Random FromTo static analysis on the current Layout first.",
    ),
    (
        "2D Vehicle Simulation 실행 · 센터라인 주행 및 10초 Pickup/Setdown",
        "2D Vehicle Simulation · centerline travel with 10-second pickup/setdown",
    ),
    ("모든 Job의 Setdown 완료", "All Jobs completed setdown"),
    ("센터라인 주행", "Centerline travel"),
    ("애니메이션 Vehicle 수", "Animation Vehicle Count"),
    ("2D Vehicle Simulation 시작", "Start 2D Vehicle Simulation"),
    ("랜덤 FromTo 필요", "Random FromTo Required"),
    ("랜덤 FromTo 모드 필요", "Random FromTo Mode Required"),
    ("2D Vehicle Simulation 시작 실패", "2D Vehicle Simulation Start Failed"),
    ("시뮬레이션할 Layout이 없습니다.", "No Layout is available for simulation."),
    ("실행 준비 완료", "Ready"),
    ("Pickup 10초", "Pickup 10 s"),
    ("Setdown 10초", "Setdown 10 s"),
    ("이적재 남은 시간", "Transfer time remaining"),
    ("공차→Pickup", "Empty→Pickup"),
    ("적재→Setdown", "Loaded→Setdown"),
    ("Edge 대기", "Edge wait"),
    ("일시정지", "Pause"),
    ("계속 실행", "Resume"),
    ("처음부터", "Restart"),
    ("배속", "Speed"),
]


def install_vehicle_simulation_english(_base_module: Any = None) -> None:
    """Register translations before the periodic English UI pass starts."""

    existing = {source for source, _target in english_ui_patch._TRANSLATIONS}
    for source, target in _TRANSLATIONS:
        if source not in existing:
            english_ui_patch._TRANSLATIONS.append((source, target))
            existing.add(source)
    english_ui_patch._TRANSLATIONS.sort(key=lambda item: len(item[0]), reverse=True)
