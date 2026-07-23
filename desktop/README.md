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

`feature/랜덤-FromTo-Vehicle-경로주행` 브랜치에서는 랜덤 From-To/LA Heatmap과 Vehicle 중앙선 경로주행 미리보기를 함께 실행할 수 있습니다. 기존 UI 원본은 `app.py`에 유지됩니다.

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
| Facility Station 기반 랜덤 From-To/Scenario 생성 | 네이티브 구현 |
| 방향성 Dijkstra Edge 통행량 Heatmap 팝업 | 네이티브 구현 |
| Random From-To Vehicle 중앙선 경로주행 미리보기 | 네이티브 구현 |
| DXF → 방향성 Graph JSON | 실제 변환·화면 미리보기·저장 연결 |
| Graph 전용 확대 팝업 | 네이티브 구현 |
| Edge 클릭·드래그 블록 선택 | 네이티브 구현 |
| 선택 Edge 방향 반전 | Graph JSON에 반영 |
| Bottleneck/ROI/Policy A-B/Digital Twin | 프로토타입 계약, Core 미연결 |

실행 결과는 `%USERPROFILE%\Documents\Sim_Core\Runs` 아래에 실행별로 저장됩니다. 랜덤 From-To 생성 결과는 `%USERPROFILE%\Documents\Sim_Core\Generated` 아래의 새 폴더에 CSV, Scenario JSON, LA 분석 JSON으로 함께 저장되며 기존 결과를 덮어쓰지 않습니다.

Windows 패키징 과정에서는 DXF 변환, 랜덤 From-To, Vehicle 중앙선 경로 기하, C++ Core, 기본 Workbench, Graph UI 및 Heatmap/Vehicle 팝업 시험을 모두 실행합니다.

## 레이아웃만으로 랜덤 반송 분석·시뮬레이션하기

1. 왼쪽에서 `입력 · CAD`를 열고 Node, 방향성 Edge, Station이 포함된 `Facility JSON`을 선택합니다.
2. `시간당 총 반송수`를 입력합니다. 예를 들어 `1,000`이면 1시간 동안 1,000건의 Job을 생성합니다(최대 10,000건).
3. 필요하면 재현용 `Random Seed`를 바꿉니다. 같은 Facility·반송수·Seed는 항상 같은 From-To를 만듭니다.
4. `랜덤 From-To 생성 · 정적분석`을 누릅니다.
5. 방향성으로 도달 가능한 서로 다른 Station 쌍에서 활성 OD를 무작위 선택하고, 총 반송수를 그 OD들에 무작위 배분합니다. 중복 From-To는 CSV에서 하나의 OD 수요로 합산합니다.
6. 팝업에서 모든 Edge를 확인합니다. 통행량이 낮거나 0인 Edge는 초록색, 최대 통행량 Edge는 빨간색이며 중간 부하는 노란색을 거칩니다.
7. 같은 팝업에서 Vehicle이 자동으로 주행을 시작합니다. `Vehicle 주행 시작/일시정지`, `처음부터`, `60x/300x/1200x` 재생 속도를 사용할 수 있습니다.
8. Vehicle의 논리 위치는 자유로운 X/Y가 아니라 `현재 Edge + 해당 Edge 진행률`입니다. 화면 X/Y와 방향은 매 프레임 Edge의 `polyline_um` 중앙선에서 계산하므로 직선·곡선·분기 모두 경로 선에 구속됩니다.
9. 대형 반송량에서도 UI가 멈추지 않도록 애니메이션은 생성 Job 중 최대 300대를 시간축 전체에서 균등 샘플링해 표시합니다. Scenario/From-To 데이터 자체의 Job 수는 줄이지 않습니다.
10. 생성된 Scenario와 From-To CSV는 화면 입력에 자동 연결됩니다. 이후 `시뮬레이션`에서 그대로 실행하거나 `Flow 분석`에서 Core 결과를 다시 확인할 수 있습니다.

최단경로는 Core와 동일하게 Edge 자유주행시간을 비용으로 사용하는 방향성 Dijkstra로 계산하며, 비용이 같은 경로는 Edge ID 순서로 결정론적으로 선택합니다. 방향 때문에 어떤 다른 Station에도 갈 수 없는 Station은 랜덤 후보에서 제외하고 화면에 제외 개수를 표시합니다. DXF Graph에는 Station ID와 연결 Node 계약이 없으므로 이 기능은 Canonical Facility JSON을 기준으로 동작합니다.

자동 생성 Scenario는 임의의 Fleet 규모가 분석 결과를 바꾸지 않도록 Job마다 From Station에 대기 중인 합성 Vehicle 1대를 배치합니다. 따라서 이 Scenario는 레이아웃 방향·경로와 Core 실행 가능성을 확인하기 위한 것이며, 필요한 실제 OHT 대수나 Dispatch 성능을 산정하는 Fleet-sizing 결과로 사용하면 안 됩니다. Job은 첫 1시간에 투입되고, 마지막 Job이 이동·Load·Unload를 끝낼 수 있는 최소 정리시간을 Scenario 종료시간에 자동으로 더합니다.

대형 레이아웃의 메모리와 분석 파일 크기가 반송수에 비례해 폭증하지 않도록 활성 OD는 `Station 수 × 4`를 기본으로 최소 64개, 최대 1,000개까지만 선택합니다(도달 가능한 OD 또는 총 반송수가 더 적으면 그 수가 상한). 입력한 총 반송수와 생성 Job 수는 줄이지 않고 선택된 OD별 빈도로 합산합니다.

저장되는 `random_la_analysis.json`에는 Heatmap 재현에 필요한 Edge 집계, OD별 거리·시간·Edge 개수는 남기되 수천 개의 Edge ID 경로 배열과 Edge별 기여 OD ID 반복 목록은 중복 저장하지 않습니다. 전체 경로가 필요하면 함께 저장된 Scenario와 From-To CSV를 `sim-core analyze`에 입력해 동일 Seed 경로를 다시 산출할 수 있습니다.

## Vehicle 중앙선 구속 원리

```text
Random From-To
    ↓
Dijkstra route edge_ids
    ↓
현재 Edge 선택
    ↓
Edge length / speed로 진행률 계산
    ↓
Edge polyline_um의 arc-length 보간
    ↓
Vehicle X/Y + tangent heading 렌더링
```

Vehicle의 화면 좌표를 `x += vx * dt`, `y += vy * dt` 형태로 독립 적분하지 않습니다. Edge 끝에 도달하면 다음 `edge_id`의 진행률 0으로 전환하므로 분기점에서도 다음 방향성 Edge의 중앙선에서 바로 주행을 이어갑니다.

## DXF Graph 만들기

1. 왼쪽에서 `입력 · CAD`를 엽니다.
2. `CAD 원본`의 `파일 선택`에서 `.dxf` 파일을 고릅니다.
3. 선택과 동시에 LINE·ARC geometry를 Node와 방향성 Edge로 변환해 아래 화면에 표시합니다.
4. 필요하면 Rail Layer, ARC 분할 수, 좌표 반올림 값을 바꾸고 `DXF 다시 변환`을 누릅니다.
5. 메인 캔버스에서 Edge를 클릭하거나 빈 영역에서 마우스를 드래그해 여러 Edge를 블록으로 선택합니다.
6. `선택 방향 반전`을 누르면 선택된 방향성 Edge의 `dir` 값이 반대로 변경됩니다.
7. 넓게 보고 싶으면 `그래프만 크게 보기`를 눌러 Graph 전용 팝업을 엽니다. 팝업에서도 선택과 방향 반전이 가능합니다.
8. `Graph JSON 저장`으로 `<원본명>.graph.json`을 저장하면 수동 방향 수정 내용까지 저장됩니다.

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

변환기 및 Random Flow 단위 시험:

```powershell
py desktop\test_dxf_graph_converter.py
py desktop\test_random_flow_analysis.py
py desktop\test_random_flow_animation.py
```
