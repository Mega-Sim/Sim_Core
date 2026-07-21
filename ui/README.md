# Sim_Core Flow Workbench

Flow Workbench는 Sim_Core의 현재 기능과 향후 기능을 한 화면에서 시험하기 위한 로컬 UI입니다.

- 1–3차에 구현된 `validate`, `analyze`, `run`은 실제 C++ `sim-core` 실행 파일을 호출합니다.
- CAD Import, Bottleneck Intelligence, ROI Reduction, Policy A/B, Digital Twin Projection은 **UI 프로토타입**입니다. 입력과 출력 계약을 만들 수 있지만 아직 Core 계산 결과가 아니라는 사실을 화면에 표시합니다.
- Facility JSON을 브라우저에서 2D 네트워크로 표시하고, 3차 분석 결과가 있으면 edge flow를 색상과 굵기로 겹쳐 표시합니다.
- 외부 Python 패키지나 프론트엔드 빌드 도구가 필요하지 않습니다.

## 실행

저장소 루트에서 Core를 먼저 빌드합니다.

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel
ctest --test-dir build --output-on-failure
```

UI를 실행합니다.

```bash
python3 ui/run_ui.py
```

Windows PowerShell 또는 Git Bash에서는 Python Launcher를 사용하는 다음 명령을 권장합니다.

```powershell
py ui/run_ui.py
```

Windows에서 Visual Studio C++ Build Tools를 사용하는 전체 빌드·실행 예시는 다음과 같습니다.

```powershell
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release
py ui/run_ui.py
```

기본 브라우저에서 `http://127.0.0.1:8765`가 열립니다. 브라우저 자동 실행이 필요 없으면 다음과 같이 실행합니다.

```bash
python3 ui/run_ui.py --no-browser
```

Core가 다른 위치에 있다면 실행 파일 경로를 지정할 수 있습니다.

```bash
SIM_CORE_BIN=/absolute/path/to/sim-core python3 ui/run_ui.py
```

## 처음 확인할 흐름

1. UI가 열리면 `examples/cross_domain` 샘플을 자동으로 불러옵니다.
2. 워크스페이스에서 Node, Edge, Station 네트워크를 확인합니다.
3. `Flow 분석 실행`을 눌러 실제 `sim-core analyze` 결과를 만듭니다.
4. Flow 분석 화면에서 edge 집중도와 station capacity를 확인합니다.
5. Simulation 화면에서 실제 `sim-core run`을 실행하고 manifest를 확인합니다.
6. Future Lab에서 A5 이후 기능의 입력·출력 계약을 먼저 시험합니다.

## 현재 기능과 프로토타입의 경계

| UI 기능 | 연결 상태 | 결과의 의미 |
|---|---|---|
| Canonical Layout 2D Preview | UI 구현 | 실제 Facility JSON 표시 |
| Model Validation | Core 연결 | `sim-core validate` 실제 결과 |
| Cross-Domain / Flow Intelligence | Core 연결 | `sim-core analyze` 실제 결과 |
| Deterministic DES | Core 연결 | `sim-core run` 실제 결과 |
| CAD Import | 프로토타입 | 파일·좌표·레이어 매핑 계약만 생성 |
| Bottleneck Intelligence | 프로토타입 | 화면 검증용 가설 점수이며 A5 판정값이 아님 |
| ROI Reduction | 프로토타입 | 축소 요청 JSON만 생성 |
| Policy A/B | 프로토타입 | 비교 실험 계약 JSON만 생성 |
| Digital Twin Projection | 프로토타입 | USD 투영 요청 JSON만 생성 |

## 입력 파일

- Facility: Canonical Facility JSON `1.0.0` 또는 `1.1.0`
- Scenario: Scenario JSON `1.0.0` 또는 `1.1.0`
- From-To: `id,from_station_id,to_station_id,expected_moves_per_hour` CSV
- CAD: DXF, DWG, STEP, STP, IFC 파일 정보. 현재 CAD geometry는 변환하지 않습니다.

브라우저는 파일 내용을 JSON 요청으로 로컬 서버에 전달합니다. 서버는 임의 경로나 임의 CLI 인자를 받지 않고, `.sim_core_ui/runs/<run-id>` 아래에 실행별 입력과 결과를 분리합니다. 7일이 지난 실행 폴더는 UI 시작 시 정리됩니다.

## 개발 참여 지점

구조는 의존성이 적은 세 파일로 나뉩니다.

```text
ui/
├── run_ui.py          # 로컬 서버와 sim-core CLI bridge
└── web/
    ├── index.html     # 화면과 입력 계약
    ├── styles.css     # 시각 디자인
    └── app.js         # 파일 처리, 네트워크 표시, Core 실행, 프로토타입
```

Core 기능이 추가되면 다음 순서로 연결합니다.

1. `run_ui.py`의 허용된 action과 CLI 인자를 명시적으로 확장합니다.
2. `/api/status`의 capability를 `prototype`에서 `available`로 변경합니다.
3. `app.js`의 프로토타입 계약 생성 함수를 실제 API 실행으로 교체합니다.
4. 화면의 `UI 프로토타입` 표시를 `CORE 연결`로 변경합니다.
