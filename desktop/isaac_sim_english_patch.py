"""English translation coverage for the NVIDIA Isaac Sim modeling workflow."""
from __future__ import annotations

import english_ui_patch as english


_ISAAC_TRANSLATIONS = [
    (
        "현재 Sim_Core CAD Graph 또는 AutoMod pm.asy를 Isaac Sim에서 바로 열 수 있는 USDA Stage로 변환합니다.",
        "Convert the current Sim_Core CAD Graph or AutoMod pm.asy into a USDA Stage that opens directly in Isaac Sim.",
    ),
    (
        "AutoMod_Isaacsim의 pm.asy → 미터 단위 방향성 Layout JSON 구조를 가져와 ",
        "Use the AutoMod_Isaacsim pm.asy → meter-based directed Layout JSON structure to ",
    ),
    (
        "현재 단계는 러프 모델링용입니다. 레일/스테이션 배치까지 생성하고 OHT·AMR 3D Asset 연결과 물리 속성은 다음 단계에서 확장합니다.",
        "This stage provides rough modeling. It generates rail and station placement; OHT/AMR 3D assets and physics properties will be expanded in the next stage.",
    ),
    (
        "현재 작업 중인 CAD Graph를 그대로 사용하거나 기존 AutoMod model.arc의 pm.asy를 불러올 수 있습니다.",
        "Use the current CAD Graph directly or load pm.asy from an existing AutoMod model.arc.",
    ),
    (
        "좌표를 meter로 정규화하고 방향성 Guide Path, Station, Routing Point를 분리합니다.",
        "Normalize coordinates to meters and separate directed Guide Paths, Stations, and Routing Points.",
    ),
    (
        "Guide Path는 BasisCurves, Station은 placeholder Cube로 구성한 isaac_stage.usda를 생성합니다.",
        "Generate isaac_stage.usda with Guide Paths as BasisCurves and Stations as placeholder Cubes.",
    ),
    (
        "Isaac Sim Script Editor에서 Stage를 여는 load_in_isaac_sim.py를 함께 생성합니다.",
        "Also generate load_in_isaac_sim.py for opening the Stage from the Isaac Sim Script Editor.",
    ),
    (
        "Isaac Sim에서 isaac_stage.usda를 열거나 Script Editor에서 load_in_isaac_sim.py를 실행해 주세요.",
        "Open isaac_stage.usda in Isaac Sim or run load_in_isaac_sim.py from the Script Editor.",
    ),
    (
        "입력 · CAD 메뉴에서 DXF/Rail을 먼저 Graph로 변환해 주세요.",
        "Convert a DXF/Rail file to a Graph first from the Input · CAD menu.",
    ),
    (
        "AutoMod pm.asy를 Isaac Sim 모델링 소스로 변환했습니다.",
        "Converted AutoMod pm.asy into an Isaac Sim modeling source.",
    ),
    (
        "현재 CAD Graph를 Isaac Sim 모델링 소스로 연결했습니다.",
        "Connected the current CAD Graph as the Isaac Sim modeling source.",
    ),
    (
        "소스를 선택하면 Node / Edge / Station 수와 변환 상태가 표시됩니다.",
        "Select a source to display Node / Edge / Station counts and conversion status.",
    ),
    (
        "소스 미선택 · CAD Graph 또는 pm.asy를 선택해 주세요.",
        "No source selected · Select a CAD Graph or pm.asy.",
    ),
    (
        "Graph와 AutoMod 레이아웃을 Isaac Sim Stage로 변환합니다",
        "Convert Graph and AutoMod layouts into an Isaac Sim Stage",
    ),
    ("Isaac Sim 모델링 · Rough Pipeline", "Isaac Sim Modeling · Rough Pipeline"),
    ("모델 소스 선택", "Select Model Source"),
    ("현재 CAD Graph 사용", "Use Current CAD Graph"),
    ("AutoMod pm.asy 선택", "Select AutoMod pm.asy"),
    ("Isaac Sim 모델 패키지 생성", "Generate Isaac Sim Model Package"),
    ("Isaac Sim 모델 생성 완료", "Isaac Sim Model Generation Completed"),
    ("Isaac Sim 모델 생성", "Generate Isaac Sim Model"),
    ("CAD Graph 또는 AutoMod pm.asy를 먼저 선택해 주세요.", "Select a CAD Graph or AutoMod pm.asy first."),
    ("Isaac Sim 모델 출력 상위 폴더 선택", "Select Parent Folder for Isaac Sim Model Output"),
    ("CAD Graph 필요", "CAD Graph Required"),
    ("Isaac 변환 실패", "Isaac Conversion Failed"),
    ("pm.asy 변환 실패", "pm.asy Conversion Failed"),
    ("모델 소스 필요", "Model Source Required"),
    ("Isaac 모델 생성 실패", "Isaac Model Generation Failed"),
    ("현재 CAD Graph · ", "Current CAD Graph · "),
    ("현재 CAD Graph", "Current CAD Graph"),
    ("선택 완료 · ", "Selected · "),
    ("Isaac Sim 모델 생성 완료 · ", "Isaac Sim Model Generation Completed · "),
    (" 좌표는 [x, y] 형식이어야 합니다.", " coordinates must be in [x, y] format."),
    (" 좌표가 숫자가 아닙니다.", " coordinates are not numeric."),
    (" 좌표에는 NaN 또는 무한대를 사용할 수 없습니다.", " coordinates cannot contain NaN or infinity."),
    ("지원하지 않는 Graph 좌표 단위입니다:", "Unsupported Graph coordinate unit:"),
    (" endpoint 참조가 올바르지 않습니다.", " endpoint reference is invalid."),
    (" endpoint가 올바르지 않습니다.", " endpoint is invalid."),
    ("에 확정된 진행 방향이 없습니다.", " does not have a resolved travel direction."),
    ("현재 Graph에 Node가 없습니다.", "The current Graph has no Nodes."),
    ("현재 Graph에 Edge가 없습니다.", "The current Graph has no Edges."),
    (" 형식이 올바르지 않습니다.", " format is invalid."),
    ("Graph metadata에서 Station label을 찾지 못했습니다.", "No Station labels were found in the Graph metadata."),
    ("GPATH 파싱 실패:", "Failed to parse GPATH:"),
    ("pm.asy에서 GPATH를 찾지 못했습니다.", "No GPATH records were found in pm.asy."),
]


def install_isaac_sim_english() -> None:
    """Extend the existing English-only runtime translator with Isaac Sim text."""

    if getattr(english, "_isaac_sim_english_installed", False):
        return
    english._isaac_sim_english_installed = True
    english._TRANSLATIONS.extend(_ISAAC_TRANSLATIONS)
    english._TRANSLATIONS.sort(key=lambda item: len(item[0]), reverse=True)
