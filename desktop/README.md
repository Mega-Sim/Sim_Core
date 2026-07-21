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
py desktop\app.py
```

Core 기능까지 연결하려면 먼저 C++ Core를 빌드합니다.

```powershell
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release
py desktop\app.py
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
| Bottleneck/ROI/Policy A-B/Digital Twin | 프로토타입 계약, Core 미연결 |

실행 결과는 `%USERPROFILE%\Documents\Sim_Core\Runs` 아래에 실행별로 저장됩니다.

Windows 패키징 과정에서는 `desktop/smoke_test.py`가 화면 없이 네이티브 UI를 실행한 뒤, 포함된 `sim-core.exe`로 Cross-Domain 샘플을 분석하고 Flow 결과가 UI 표에 연결되는지 자동 확인합니다.

## DXF Graph 만들기

1. 왼쪽에서 `입력 · CAD`를 엽니다.
2. `CAD 원본`의 `파일 선택`에서 `.dxf` 파일을 고릅니다.
3. 선택과 동시에 LINE·ARC geometry를 Node와 방향성 Edge로 변환해 아래 화면에 표시합니다.
4. 필요하면 Rail Layer, ARC 분할 수, 좌표 반올림 값을 바꾸고 `DXF 다시 변환`을 누릅니다.
5. `Graph JSON 저장`으로 `<원본명>.graph.json`을 저장합니다.

Rail Layer를 비워 두면 모든 LINE·ARC Layer를 읽습니다. 여러 Layer는 쉼표 또는 세미콜론으로 구분합니다. 화면에서 마우스 휠로 확대·축소하고 드래그로 이동할 수 있으며, Node와 Edge 위에 마우스를 올리면 ID와 추정 방향을 확인할 수 있습니다.

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
```
