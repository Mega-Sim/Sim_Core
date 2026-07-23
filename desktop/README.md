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
| DXF / SemiLA `.rail` → 방향성 Rail Graph JSON | 실제 변환·화면 미리보기·저장 연결 |
| Graph 전용 확대 팝업 | 네이티브 구현 |
| Edge 클릭·드래그 블록 선택 | 네이티브 구현 |
| 선택 Edge 방향 반전 | Graph JSON에 반영 |
| Bottleneck/ROI/Policy A-B/Digital Twin | 프로토타입 계약, Core 미연결 |

실행 결과는 `%USERPROFILE%\Documents\Sim_Core\Runs` 아래에 실행별로 저장됩니다.

Windows 패키징 과정에서는 `desktop/smoke_test.py`와 `desktop/graph_ui_smoke_test.py`를 실행해 기본 Workbench와 Graph UI 개선 기능을 자동 확인합니다.

## DXF / Rail Graph 만들기

1. 왼쪽에서 `입력 · CAD`를 엽니다.
2. `CAD / Rail`의 `파일 선택`에서 `.dxf` 또는 SemiLA `.rail` 파일을 고릅니다.
3. DXF는 LINE·ARC를 경량 Rail Graph로 변환하고, `.rail`은 저장된 NODE/LINK/RAILLIST를 바로 읽어 표시합니다.
4. DXF라면 필요에 따라 Rail Layer, ARC 표시 분할 수, 좌표 반올림 값을 바꾸고 `Rail Graph 다시 변환`을 누릅니다.
5. 메인 캔버스에서 Edge를 클릭하거나 빈 영역에서 마우스를 드래그해 여러 Edge를 블록으로 선택합니다.
6. `선택 방향 반전`을 누르면 선택된 방향성 Edge의 `dir` 값이 반대로 변경됩니다.
7. 넓게 보고 싶으면 `그래프만 크게 보기`를 눌러 Graph 전용 팝업을 엽니다. 팝업에서도 선택과 방향 반전이 가능합니다.
8. `Graph JSON 저장`으로 `<원본명>.graph.json`을 저장하면 수동 방향 수정 내용까지 저장됩니다.

Rail Layer를 비워 두면 모든 LINE·ARC Layer를 읽습니다. 여러 Layer는 쉼표 또는 세미콜론으로 구분합니다. 기존 파일 카드의 장식용 Badge/Icon 영역은 Graph 화면 공간 확보를 위해 축소되며, Graph 캔버스의 최소 높이를 확장합니다.

방향은 CAD geometry의 연결성과 진행 벡터를 이용한 추정값입니다. 실제 OHT 운행 방향 데이터와 반드시 대조한 뒤 시뮬레이션 입력으로 승격해야 합니다.

대형 FAB 도면의 ARC는 처음부터 하나의 논리 Rail Edge로 유지합니다. ARC를 여러 임시 Edge로 만든 뒤 DXF를 다시 읽어 합치던 단계가 없으며, 분기점이 실제 ARC 내부에 닿을 때만 그 지점에서 나눕니다. 대형 미리보기는 Edge·화살표·Node를 소수의 Qt 일괄 경로로 렌더링하고, 영역 선택은 좌표 기반으로 처리합니다. AutoMod PM 생성은 이 빠른 Rail 미리보기와 분리된 후단 단계입니다.

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
py desktop\test_rail_file.py
```
