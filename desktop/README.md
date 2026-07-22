# Sim_Core Native Desktop Workbench

웹 서버나 HTTP 통신을 사용하지 않는 Windows 데스크톱 UI입니다. Qt 위젯으로 직접 화면을 그리고 `QProcess`로 C++ `sim-core.exe`를 호출합니다.

## 가장 쉬운 사용법

GitHub Actions의 `Sim_Core Native Desktop - Windows EXE` 실행 결과에서 `Sim_Core_Flow_Workbench-windows-x64` Artifact를 내려받아 압축을 풉니다.

```text
Sim_Core_Flow_Workbench.exe
```

위 파일을 더블클릭하면 됩니다. 별도의 Python, CMake 설치나 웹 브라우저가 필요하지 않습니다. 패키지 안에는 현재 브랜치에서 빌드한 `sim-core.exe`와 Cross-Domain 샘플이 포함됩니다.

## 개발 중 직접 실행

Python이 설치된 Windows에서:

```powershell
py -m pip install -r desktop\requirements.txt
py desktop\app_wrapper.py
```

`feature/Graph-생성-UI-개선` 브랜치에서는 `app_wrapper.py`가 기존 Workbench에 Graph 생성 UI 개선 기능을 적용합니다. 기존 UI 원본은 `app.py`에 유지됩니다.

Core 기능까지 연결하려면 먼저 C++ Core를 빌드합니다.

```powershell
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release
py desktop\app_wrapper.py
```

## 단일 EXE 직접 생성

Visual Studio 2022 C++ Build Tools, CMake, Python이 설치된 Windows PowerShell에서:

```powershell
powershell -ExecutionPolicy Bypass -File desktop\build_windows.ps1
```

결과:

```text
dist\Sim_Core_Flow_Workbench.exe
```

## 구현 경계

| 기능 | 상태 |
|---|---|
| Facility/Scenario/From-To 파일 선택 | 네이티브 구현 |
| Canonical Network 2D 표시 | 네이티브 구현 |
| `sim-core validate` | 실제 Core 연결 |
| `sim-core analyze` | 실제 Core 연결 |
| `sim-core run` | 실제 Core 연결 |
| DXF → 방향성 Graph JSON | 실제 변환·화면 미리보기·저장 연결 |
| 방향성 Graph → AutoMod `model.arc` | `pm.asy`·`model~.asy`·`model.amo` 생성 및 연결 |
| Graph 전용 확대 팝업 | 네이티브 구현 |
| Edge 클릭·드래그 블록 선택 | 네이티브 구현 |
| 선택 Edge 방향 반전 | Graph JSON에 반영 |
| Bottleneck/ROI/Policy A-B/Digital Twin | 프로토타입 계약, Core 미연결 |

실행 결과는 `%USERPROFILE%\Documents\Sim_Core\Runs` 아래에 실행별로 저장됩니다.

Windows 패키징 과정에서는 `desktop/smoke_test.py`와 `desktop/graph_ui_smoke_test.py`를 실행해 기본 Workbench와 Graph UI 개선 기능을 자동 확인합니다.

## DXF Graph 만들기

1. 왼쪽에서 `입력 · CAD`를 엽니다.
2. `CAD 원본`의 `파일 선택`에서 `.dxf` 파일을 고릅니다.
3. 선택과 동시에 LINE·ARC geometry를 Node와 방향성 Edge로 변환해 아래 화면에 표시합니다.
4. 필요하면 Rail Layer, ARC 분할 수, 좌표 반올림 값을 바꾸고 `DXF 다시 변환`을 누릅니다.
5. 메인 캔버스에서 Edge를 클릭하거나 빈 영역에서 마우스를 드래그해 여러 Edge를 블록으로 선택합니다.
6. `선택 방향 반전`을 누르면 선택된 방향성 Edge의 `dir` 값이 반대로 변경됩니다.
7. 넓게 보고 싶으면 `그래프만 크게 보기`를 눌러 Graph 전용 팝업을 엽니다. 팝업에서도 선택과 방향 반전이 가능합니다.
8. `Graph JSON 저장`으로 `<원본명>.graph.json`을 저장하면 수동 방향 수정 내용까지 저장됩니다.
9. 바로 옆의 `AutoMod 모델변환`을 누르고 상위 폴더를 선택하면 그 안에 현재 방향과 곡선 형상을 반영한 `model.arc` 폴더를 생성합니다.

Rail Layer를 비워 두면 모든 LINE·ARC Layer를 읽습니다. 여러 Layer는 쉼표 또는 세미콜론으로 구분합니다. 기존 파일 카드의 장식용 Badge/Icon 영역은 Graph 화면 공간 확보를 위해 축소되며, Graph 캔버스의 최소 높이를 확장합니다.

방향은 CAD geometry의 연결성과 진행 벡터를 이용한 추정값입니다. 실제 OHT 운행 방향 데이터와 반드시 대조한 뒤 시뮬레이션 입력으로 승격해야 합니다.

UI 없이 직접 변환할 수도 있습니다.

```powershell
py desktop\dxf_graph_converter.py layout.dxf `
  --layer OHT_RAIL_CENTER `
  --arc-segments 10 `
  --precision 3 `
  --unit millimeter `
  --output layout.graph.json
```

변환기 단위 시험:

```powershell
py desktop\test_dxf_graph_converter.py
py desktop\test_automod_pm_converter.py
```

이미 저장된 Graph JSON은 UI 없이도 변환할 수 있습니다.

```powershell
py desktop\automod_pm_converter.py layout.graph.json --output model.arc
```

출력 폴더에는 정확히 `model.amo`, `model~.asy`, `pm.asy`가 생성됩니다.
`model.amo`는 `MOVESYS name pm`과 `PROCSYS name model~`으로 두 System을 연결합니다.
`model~.asy`는 아직 Process 및 소스코드가 없는 빈 Process System이며 `.m`, `.c`,
`.h`, `model.dir`은 만들지 않습니다. AutoMod에서 `model.amo`를 열고 빌드하면
`model.dir`이 생성됩니다.

`pm.asy`는 AutoMod 12.6 AGVS System 형식이며 좌표는 `Millimeters`입니다.
Control Point는 모든 Graph Node에 만들지 않고 CAD의 `station-*` TEXT/MTEXT 위치에만
Station Control Point로 생성합니다. 진행 방향 기준으로 Edge가 두 갈래 이상으로
갈라지는 Node에는 진입 Edge 끝의 정확히 10 mm 전 위치에 `branch_*` Control Point를
하나 추가합니다. Branch 크기는 Station의 1/3입니다. 일반 곡선 접점과 합류점에는
Control Point를 추가하지 않습니다. 차량 수는 0으로 두므로
AutoMod에서 모델을 연 뒤 차량 종류·수량과 운행 로직을 추가할 수 있습니다.
Graph에서 하나로 통합된 DXF ARC Edge는 AutoMod에서도 중심점과 회전각을 가진
반지름 450 mm의 단일 원호 `GPATH`로 생성됩니다. 450 mm 원호와 일치하지 않는
곡선은 여러 직선으로 대체하지 않고 변환 오류로 차단합니다. Control Point 크기는
기본값의 1/5로 출력합니다. AutoMod 방향 표식은 ASY 크기 속성이 없으므로 원호당
여러 표식이 겹치지 않도록 논리 ARC 하나당 단일 `GPATH`만 생성합니다. `nav` 값은
표식 크기가 아닌 차량의 경로 탐색 비용이므로 기본값 1을 유지합니다.
