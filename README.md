# Sim_Core

Sim_Core는 FAB 물류, 특히 OHT 운영 정책을 실험하기 위한 **차세대 독립 이산사건 시뮬레이션 코어이자 Digital Twin-ready 플랫폼**입니다.

이 저장소의 목표는 기존 OHT Emulator, OCS, OCS Replay 또는 특정 상용 시뮬레이터의 구조를 복제하는 것이 아닙니다. 기존 시스템과 분석 자료는 실제 운영 요구사항과 실패 사례를 식별하기 위한 참고 자료로만 사용하며, 필요한 기능은 Sim_Core 고유의 현대적이고 일반화된 구조로 다시 설계합니다.

또한 Sim_Core는 현재 GPU와 고성능 HW 접근성이 제한된 환경에서도 완전한 Headless Simulation을 수행할 수 있어야 하며, 향후 로컬 또는 Cloud GPU가 확보되었을 때 동일 Canonical Model과 Runtime 결과를 별도의 재모델링 없이 Omniverse/Isaac Sim 기반 Digital Twin으로 전환할 수 있도록 설계합니다.

주요 목표는 다음과 같습니다.

- 다양한 레이아웃과 운영 데이터를 중립적인 Canonical Facility Model로 변환 및 검증
- 동일 입력과 시드에서 동일 결과를 만드는 결정론적 DES 커널
- routing, dispatch, mobility, traffic, energy, deadlock 정책의 독립 교체와 A/B 실험
- fidelity 단계별 차량 이동 및 운동 상태 모델링
- Event Timeline, Trace Replay, Time Travel Debugging, Deterministic Rerun
- 실행 간 first divergence와 정책 결정 차이를 추적하는 Run Comparison
- 권한이 확인된 운영 기록을 시나리오로 재구성하는 Scenario Reconstruction
- source provenance와 외부 ID lineage를 위한 범용 Source Identity Mapping
- 실행 근거를 추적할 수 있는 이벤트 로그, 상태 전이, 결정 로그와 결과 지표
- GPU 없이도 완전 동작하는 고성능 Headless-first 실행 코어
- Canonical Model에서 USD/Omniverse/Isaac Sim으로 직접 투영하는 Digital Twin Projection
- Asset Binding Profile 기반의 저품질 Debug Scene부터 고충실도 Digital Twin까지 단계적 표현
- Simulation Fidelity와 Visualization Fidelity의 독립 제어
- Local CPU, Batch Server, Cloud GPU, Full Co-simulation을 동일 Model Revision으로 지원

## 현재 상태

현재 기준 설계는 `Architecture v3`입니다.

v1의 Canonical Model과 결정론적 DES, v2의 현대적 Policy/Observability 구조를 유지하면서, **HW 접근성 문제를 Core 설계에서 분리하고 향후 Omniverse/Isaac Sim Digital Twin으로 One-click 수준에서 전환할 수 있는 구조**를 핵심 아키텍처로 추가했습니다.

핵심 방향은 다음과 같습니다.

- Simulation Runtime은 GPU와 3D 엔진 없이 완전히 동작
- Canonical Model은 topology뿐 아니라 geometry, coordinate, semantic metadata를 보존
- Digital Twin Projection Layer를 공식 아키텍처 경계로 정의
- Canonical entity와 3D asset을 `AssetBindingProfile`로 분리
- Simulation Entity ID와 USD Prim Path를 `EntityPrimMap`으로 분리
- Runtime State를 공통 `EntityStateFrame` 계약으로 2D/3D/Isaac Sim에 전달
- Simulation time과 render/wall clock을 `Time Bridge`로 분리
- 결과 Replay만으로도 나중에 Cloud GPU에서 Digital Twin 재생 가능
- 실제 Isaac Sim Adapter 구현 전부터 Canonical Model을 Digital Twin-ready로 유지

목표 사용자 경험은 다음과 같습니다.

```text
Headless Simulation Model
        |
        v
[ Open in Digital Twin ]
        |
        v
USD Scene Package 자동 생성
        |
        v
Omniverse / Isaac Sim 로드
        |
        v
동일 Runtime State 또는 Replay 연결
```

- [Simulator Architecture v3](docs/architecture/SIM_CORE_ARCHITECTURE_V3.md)
- [Simulator Architecture v2](docs/architecture/SIM_CORE_ARCHITECTURE_V2.md)
- [Simulator Architecture v1](docs/architecture/SIM_CORE_ARCHITECTURE_V1.md)
- [ADR-0001: 독립 구현과 Clean-room 경계](docs/architecture/decisions/0001-independent-clean-room-boundary.md)
- [ADR-0002: 결정론적 DES와 정수 시간](docs/architecture/decisions/0002-deterministic-des-and-integer-time.md)
- [ADR-0003: Canonical Facility Model 경계](docs/architecture/decisions/0003-canonical-facility-model-boundary.md)
- [ADR-0004: C++20 헤드리스 코어](docs/architecture/decisions/0004-cpp20-headless-core.md)

## 핵심 설계 원칙

1. Legacy 시스템은 참고 자료이며 Target Architecture가 아닙니다.
2. 원본 포맷과 외부 시스템의 구조는 Adapter 밖으로 새지 않습니다.
3. 시뮬레이션 결과의 기준은 UI나 3D가 아니라 Headless Simulation Runtime입니다.
4. 모델 revision, scenario, seed, policy version, engine version이 같으면 이벤트 순서와 결과 hash가 같아야 합니다.
5. routing, dispatch, mobility, traffic 등의 운영 로직은 교체 가능한 Policy로 구성합니다.
6. 모든 주요 상태 변화와 정책 결정은 원인 event와 reason을 추적할 수 있어야 합니다.
7. Replay는 특정 OCS Replay 프로그램을 모방하지 않고 Observability와 Debugging 기능으로 설계합니다.
8. 외부 ID는 Canonical ID와 직접 혼용하지 않고 provenance 기반 Source Identity로 추적합니다.
9. 이동 충실도는 단순 이동 시간부터 연속 위치·가감속·구역 제어까지 단계적으로 높입니다.
10. GPU나 Isaac Sim이 없어도 Core Simulation 기능은 완전 동작해야 합니다.
11. Canonical Model은 향후 Digital Twin 투영에 필요한 좌표, geometry, semantic metadata를 처음부터 보존합니다.
12. USD/Omniverse/Isaac Sim은 Adapter이며 Domain과 Kernel은 특정 3D 엔진에 종속되지 않습니다.
13. Simulation Fidelity와 Visualization Fidelity를 독립적으로 선택할 수 있어야 합니다.
14. 3D asset은 Model에 직접 결합하지 않고 versioned Asset Binding Profile로 관리합니다.
15. Runtime State와 Digital Twin 표현은 versioned State Contract로 연결합니다.
16. Cloud GPU가 확보되었을 때 Model 재구축 없이 Digital Twin으로 전환 가능해야 합니다.
17. 권한이 불명확한 코드, 바이너리, UI 자산은 제품 코드에 포함하지 않습니다.

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
│   └── digital_twin/       # coordinate, asset binding, entity mapping, state contract
├── src/
│   ├── application/         # use case와 run orchestration
│   ├── domain/              # OHT, Job, Network, Resource 모델
│   ├── kernel/              # 시간, event queue, scheduler, RNG
│   ├── modules/             # routing, dispatch, mobility, traffic, energy, deadlock
│   ├── observability/       # timeline, replay, snapshot, comparison, analytics
│   ├── digital_twin/
│   │   ├── projection/      # Canonical Model -> target scene
│   │   ├── asset_binding/   # semantic entity -> 3D asset
│   │   ├── state_bridge/    # Runtime State -> Digital Twin State
│   │   └── time_bridge/     # simulation time -> render/wall clock
│   ├── ports/               # importer, store, observer, integration 인터페이스
│   └── adapters/
│       ├── file/
│       ├── integration/
│       └── digital_twin/
│           ├── usd/
│           └── isaac_sim/
└── tests/                   # unit, contract, golden, regression, projection, performance
```

Digital Twin 계층은 Domain이나 Kernel의 하위가 아니라 별도의 outward-facing projection 계층입니다.

실제 Isaac Sim Adapter 구현은 뒤 단계에서 진행할 수 있지만, Canonical coordinate contract, semantic type, geometry schema, AssetBindingProfile, EntityPrimMap, Runtime State Contract는 초기 Foundation 단계부터 Digital Twin-ready 상태로 유지합니다.

## 기준 분석 자료

[AutoMod OHT 종합 정적분석 보고서](AutoMod_OHT_Materials_Comprehensive_Analysis_2026-07-15.docx)와 권한이 확인된 Legacy OHT 관련 자료는 요구사항과 실패 사례를 식별하는 참고 자료입니다. 해당 자료의 상용 코드나 런타임 구현을 제품 코드로 복사하지 않으며, 원본 사례는 사용 권한과 보안 검토를 통과한 정제 fixture만 회귀시험에 사용합니다.
