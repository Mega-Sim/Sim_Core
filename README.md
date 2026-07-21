# Sim_Core 2차 개발

Sim_Core는 FAB 물류, 특히 OHT 운영 정책을 실험하기 위한 **차세대 독립 이산사건 시뮬레이션 코어이자 Digital Twin-ready Multi-Scale Simulation 플랫폼**입니다.

이 저장소의 목표는 기존 OHT Emulator, OCS, OCS Replay, SemiLA 또는 특정 상용 시뮬레이터의 구조를 복제하는 것이 아닙니다. 기존 시스템과 분석 자료는 실제 운영 요구사항과 실패 사례를 식별하기 위한 참고 자료로만 사용하며, 필요한 기능은 Sim_Core 고유의 현대적이고 일반화된 구조로 다시 설계합니다.

Sim_Core는 현재 GPU와 고성능 HW 접근성이 제한된 환경에서도 완전한 Headless Simulation과 정적/준정적 분석을 수행할 수 있어야 하며, 향후 로컬 또는 Cloud GPU가 확보되었을 때 동일 Canonical Model과 Runtime 결과를 별도의 재모델링 없이 Omniverse/Isaac Sim 기반 Digital Twin으로 전환할 수 있도록 설계합니다.

또한 대규모 FAB 모델을 항상 전체 규모와 전체 3D fidelity로 실행하지 않습니다. 먼저 애니메이션 없는 Bottleneck Intelligence 분석으로 병목 후보를 찾고, 관심 구간을 ROI로 추출한 뒤 외부 영역의 부하를 Boundary Contract로 보존하는 Reduced Model을 생성하여 개인 워크스테이션에서도 상세 검증할 수 있도록 설계합니다.

실제 `SemiLA_1204_EXE` 정적분석에서 확인된 요구사항은 제품 구조를 복제하지 않고 다음과 같이 일반화해 반영합니다.

- layout/topology 편집과 분석의 분리
- From-To 수요, 거리, route, capacity, storage 검증
- rail frequency와 flow 기반 병목 후보 분석
- layout, 운영 데이터, route 결과의 교차검증
- 운영 로그 기반 관측값과 모델 예측값 비교
- 병목 위험도와 근거를 애니메이션 없이 정적 Overlay로 표시
- 분석 결과를 ROI 추출 및 Model Reduction 입력으로 연결

## 주요 목표

- 다양한 레이아웃과 운영 데이터를 중립적인 Canonical Facility Model로 변환 및 검증
- 동일 입력과 시드에서 동일 결과를 만드는 결정론적 DES 커널
- routing, dispatch, mobility, traffic, energy, deadlock 정책의 독립 교체와 A/B 실험
- fidelity 단계별 차량 이동 및 운동 상태 모델링
- Event Timeline, Trace Replay, Time Travel Debugging, Deterministic Rerun
- 실행 간 first divergence와 정책 결정 차이를 추적하는 Run Comparison
- 권한이 확인된 운영 기록을 시나리오로 재구성하는 Scenario Reconstruction
- source provenance와 외부 ID lineage를 위한 범용 Source Identity Mapping
- GPU 없이도 완전 동작하는 고성능 Headless-first 실행 코어
- Canonical Model에서 USD/Omniverse/Isaac Sim으로 직접 투영하는 Digital Twin Projection
- Asset Binding Profile 기반의 저품질 Debug Scene부터 고충실도 Digital Twin까지 단계적 표현
- Simulation Scale, Simulation Fidelity, Visualization Fidelity의 독립 제어
- Local CPU, Batch Server, Cloud GPU를 동일 Model Revision으로 지원
- 애니메이션 없는 Static/Quasi-static Bottleneck Analysis와 2D Heatmap
- From-To, route, distance, rail frequency, flow, capacity, storage 기반 정적 분석
- 모델 입력과 운영 로그 사이 Cross-validation
- Bottleneck-driven ROI 자동/수동 선택
- ROI 외부 부하를 Equivalent Demand, Boundary Queue, Travel Delay Proxy로 보존하는 Model Reduction
- Full Model과 Reduced Model의 차이를 검증하는 Reduction Validation
- Reduced ROI Model 역시 One-click Digital Twin Projection 지원

## 현재 상태

현재 기준 설계는 `Architecture v5`입니다.

v1의 Canonical Model과 결정론적 DES, v2의 현대적 Policy/Observability 구조, v3의 Headless-first/One-click Digital Twin 구조, v4의 Bottleneck-driven Multi-Scale Simulation/Model Reduction을 유지하면서, **실제 SemiLA 정적분석에서 확인된 From-To·route·distance·rail frequency·flow·capacity·storage·cross-validation 요구사항을 범용 Analysis Layer로 보강**했습니다.

핵심 방향은 다음과 같습니다.

- 전체 모델은 Simulation Truth로 유지
- 전체 FAB를 먼저 Static/Quasi-static Bottleneck Analyzer로 빠르게 분석
- topology뿐 아니라 From-To 수요, shortest route, distance matrix, rail frequency, flow pressure, capacity/storage를 함께 분석
- layout, demand, route, 운영 기록 사이 불일치를 Cross-validation으로 진단
- 병목 후보를 2D Heatmap과 Risk Ranking으로 표시
- 병목 주변을 Region of Interest(ROI)로 선택
- ROI 내부는 explicit topology/vehicle/resource를 유지
- ROI 외부는 단순 삭제하지 않고 Boundary Contract로 부하 압력을 보존
- 축소율 자체보다 inflow/outflow, queue, bottleneck ranking, policy sensitivity 보존을 우선
- Full Model과 Reduced Model 관계를 Reduction Manifest로 추적
- 개인 워크스테이션에서 Reduced Model을 반복 검증한 뒤 전체 Headless 또는 Cloud GPU Digital Twin으로 승격 검증
- Reduced ROI Model도 Full Model과 동일한 Digital Twin Projection 계약을 사용

권장 검증 흐름:

```text
Full Canonical Model
        |
        v
Structural + From-To + Route + Distance Analysis
        |
        v
Rail Frequency / Flow / Capacity / Storage Analysis
        |
        v
Cross-validation with Authorized Operational Data
        |
        v
Bottleneck Heatmap + Risk Ranking
        |
        v
ROI Selection
        |
        v
Model Reduction + Boundary Contract
        |
        v
Reduced Workstation Model
        |
        v
Local Detailed Simulation / Policy A-B Test
        |
        v
Full Headless Confirmation
        |
        v
[ Open ROI in Digital Twin ] 또는 Full Digital Twin
        |
        v
Omniverse / Isaac Sim / Cloud GPU
```

- [Simulator Architecture v5](docs/architecture/SIM_CORE_ARCHITECTURE_V5.md)
- [Simulator Architecture v4](docs/architecture/SIM_CORE_ARCHITECTURE_V4.md)
- [Simulator Architecture v3](docs/architecture/SIM_CORE_ARCHITECTURE_V3.md)
- [Simulator Architecture v2](docs/architecture/SIM_CORE_ARCHITECTURE_V2.md)
- [Simulator Architecture v1](docs/architecture/SIM_CORE_ARCHITECTURE_V1.md)
- [ADR-0001: 독립 구현과 Clean-room 경계](docs/architecture/decisions/0001-independent-clean-room-boundary.md)
- [ADR-0002: 결정론적 DES와 정수 시간](docs/architecture/decisions/0002-deterministic-des-and-integer-time.md)
- [ADR-0003: Canonical Facility Model 경계](docs/architecture/decisions/0003-canonical-facility-model-boundary.md)
- [ADR-0004: C++20 헤드리스 코어](docs/architecture/decisions/0004-cpp20-headless-core.md)

## 최초 개발 Vertical Slice

설계가 코드 구조만 만든 채 오래 분리되지 않도록, 첫 개발 단위에서 다음 최소 실행 경로를 구현했습니다.

- CMake/C++20 정적 라이브러리와 Headless CLI
- versioned Canonical Facility/Scenario JSON Schema
- Node, 방향성 Edge, Station, Source Identity, 좌표·geometry 계약
- 구조·단위·geometry·graph·scenario 사전 검증
- `int64` microsecond와 `(time, priority, sequence)` 결정론적 Event Queue
- generation/tombstone 취소와 timestamp별 zero-delay guard
- 자유주행시간 기반 방향성 Dijkstra와 nearest-feasible dispatch
- F0 차량/Job 상태 전이
- 결정론적 JSONL Event Trace, Run Manifest, 최소 Trace Replay
- 단일 직선 network Golden Scenario

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel
ctest --test-dir build --output-on-failure

./build/sim-core validate \
  --facility examples/single_line/facility.json \
  --scenario examples/single_line/scenario.json

./build/sim-core run \
  --facility examples/single_line/facility.json \
  --scenario examples/single_line/scenario.json \
  --output run-output

./build/sim-core replay --trace run-output/event_trace.jsonl
```

Golden Scenario는 차량 1대와 Job 1건이 `IDLE → TO_PICKUP → LOADING → TO_DROPOFF → UNLOADING → IDLE`로 20초에 완료되며, 반복 실행 시 동일한 `trace_hash`를 생성합니다.

- [최초 Vertical Slice 개발 기준과 검증 결과](docs/development/VERTICAL_SLICE_01.md)

## 2차 개발: Cross-Domain Validation Vertical Slice

2차 개발은 Architecture v5의 `A2 Cross-Domain Validation` 품질 게이트를 실행 가능한 코드로 연결합니다.

- Facility/Scenario Schema `1.1.0`과 `1.0.0` 하위 호환 Loader
- ControlPoint, Zone, Parking, Charger, VehicleType, source geometry transform
- 정규 JSON 기반 실제 SHA-256 `content_hash` 검증
- JSON 또는 중립 From-To CSV 수요 입력
- Canonical ID와 source identity 충돌 검출
- source artifact/namespace provenance 누락 검출
- source frame과 canonical frame 사이 transform 누락·중복·target 불일치 검출
- station pose와 rail attachment node 좌표 교차검증
- From-To station 존재성·방향성 도달성·경로·거리·예상 이동시간 분석
- From-To pressure와 station capacity 사전 비교
- revision 간 hash 재사용, source identity remap, node 이동 진단
- versioned JSON 진단 리포트와 비정상 종료 코드

```bash
./build/sim-core analyze \
  --facility examples/cross_domain/facility.json \
  --scenario examples/cross_domain/scenario.json \
  --from-to-csv examples/cross_domain/from_to.csv \
  --output cross-domain-report.json
```

정상 예제는 `OD-A-C` 수요에 대해 `E-A-B → E-B-C`, 거리 `30,000,000 um`, 자유주행시간 `15,000,000 us`를 결정론적으로 산출합니다.

- [2차 Cross-Domain Validation 개발 기준과 검증 결과](docs/development/VERTICAL_SLICE_02.md)

## 핵심 설계 원칙

1. Legacy 시스템은 참고 자료이며 Target Architecture가 아닙니다.
2. 원본 포맷과 외부 시스템의 구조는 Adapter 밖으로 새지 않습니다.
3. 시뮬레이션 결과의 기준은 UI나 3D가 아니라 Headless Simulation Runtime입니다.
4. 전체 Canonical Model은 Simulation Truth이며 Reduced Model은 특정 질문을 위한 Projection입니다.
5. 모델 revision, scenario, seed, policy version, engine version이 같으면 이벤트 순서와 결과 hash가 같아야 합니다.
6. routing, dispatch, mobility, traffic 등의 운영 로직은 교체 가능한 Policy로 구성합니다.
7. 모든 주요 상태 변화와 정책 결정은 원인 event와 reason을 추적할 수 있어야 합니다.
8. Replay는 특정 OCS Replay 프로그램을 모방하지 않고 Observability와 Debugging 기능으로 설계합니다.
9. 외부 ID는 Canonical ID와 직접 혼용하지 않고 provenance 기반 Source Identity로 추적합니다.
10. GPU나 Isaac Sim이 없어도 Core Simulation과 Bottleneck Analysis 기능은 완전 동작해야 합니다.
11. 병목 분석 결과는 3D 애니메이션 없이 2D Heatmap과 정적 지표로 확인 가능해야 합니다.
12. 정적 분석은 topology만 보지 않고 From-To, route, distance, frequency, flow, capacity, storage를 함께 평가합니다.
13. 정적 분석 결과와 운영 로그는 별도 Evidence로 관리하고 Cross-validation할 수 있어야 합니다.
14. 차량 수 축소는 random sampling으로 수행하지 않고 ROI 외부 부하를 Boundary Contract로 보존합니다.
15. Reduction Ratio보다 병목 위치, queue pressure, policy sensitivity 등 목적별 특성 보존이 우선입니다.
16. Full Model과 Reduced Model의 관계는 Reduction Manifest로 항상 추적합니다.
17. 축소 모델의 신뢰성은 Reduction Validation Report로 검증합니다.
18. Canonical Model은 향후 Digital Twin 투영에 필요한 좌표, geometry, semantic metadata를 처음부터 보존합니다.
19. USD/Omniverse/Isaac Sim은 Adapter이며 Domain과 Kernel은 특정 3D 엔진에 종속되지 않습니다.
20. Simulation Scale, Simulation Fidelity, Visualization Fidelity를 독립적으로 선택할 수 있어야 합니다.
21. 3D asset은 Model에 직접 결합하지 않고 versioned Asset Binding Profile로 관리합니다.
22. Reduced ROI Model과 Full Model 모두 동일한 Digital Twin Projection 계약을 사용합니다.
23. Cloud GPU가 확보되었을 때 Model 재구축 없이 Digital Twin으로 전환 가능해야 합니다.
24. 권한이 불명확한 코드, 바이너리, UI 자산은 제품 코드에 포함하지 않습니다.

## 계획된 저장소 구조

```text
Sim_Core/
├── apps/                    # CLI와 서비스 실행 진입점
├── bindings/                # Python 및 외부 runtime 연동 경계
├── include/sim_core/        # 공개 C++ API
├── schemas/
│   ├── facility/
│   ├── scenario/
│   ├── runtime/
│   ├── observability/
│   ├── analysis/            # from-to, route, distance, flow, capacity, evidence
│   ├── bottleneck/          # candidate, overlay, analysis result
│   ├── reduction/           # ROI, boundary, manifest, validation
│   └── digital_twin/        # coordinate, asset binding, entity mapping, state contract
├── src/
│   ├── application/         # use case와 run orchestration
│   ├── domain/              # OHT, Job, Network, Resource 모델
│   ├── kernel/              # 시간, event queue, scheduler, RNG
│   ├── modules/             # routing, dispatch, mobility, traffic, energy, deadlock
│   ├── analysis/
│   │   ├── structural/
│   │   ├── from_to/
│   │   ├── route_distance/
│   │   ├── frequency_flow/
│   │   ├── capacity_storage/
│   │   ├── cross_validation/
│   │   └── bottleneck/
│   ├── reduction/
│   │   ├── roi/
│   │   ├── boundary/
│   │   ├── aggregation/
│   │   └── validation/
│   ├── observability/       # timeline, replay, snapshot, comparison, analytics
│   ├── digital_twin/
│   │   ├── projection/      # Canonical/Reduced Model -> target scene
│   │   ├── asset_binding/
│   │   ├── state_bridge/
│   │   └── time_bridge/
│   ├── ports/
│   └── adapters/
│       ├── file/
│       ├── integration/
│       └── digital_twin/
│           ├── usd/
│           └── isaac_sim/
└── tests/
    ├── unit/
    ├── contract/
    ├── golden/
    ├── analysis/
    ├── reduction/
    ├── equivalence/
    ├── projection/
    └── performance/
```

## 기준 분석 자료

[AutoMod OHT 종합 정적분석 보고서](AutoMod_OHT_Materials_Comprehensive_Analysis_2026-07-15.docx)와 권한이 확인된 Legacy OHT 관련 자료는 요구사항과 실패 사례를 식별하는 참고 자료입니다. `SemiLA_1204_EXE` 정적분석에서 확인된 기능도 요구사항 수준으로만 참고하며, 해당 제품의 내부 구현, UI, 클래스 구조, 템플릿을 제품 코드로 복제하지 않습니다. 원본 사례는 사용 권한과 보안 검토를 통과한 정제 fixture만 회귀시험에 사용합니다.
