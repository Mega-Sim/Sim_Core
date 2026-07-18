# Sim_Core

Sim_Core는 FAB 물류, 특히 OHT 운영 정책을 실험하기 위한 **차세대 독립 이산사건 시뮬레이션 코어**입니다.

이 저장소의 목표는 기존 OHT Emulator, OCS, OCS Replay 또는 특정 상용 시뮬레이터의 구조를 복제하는 것이 아닙니다. 기존 시스템과 분석 자료는 실제 운영 요구사항과 실패 사례를 식별하기 위한 참고 자료로만 사용하며, 필요한 기능은 Sim_Core 고유의 현대적이고 일반화된 구조로 다시 설계합니다.

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
- 2D/3D 및 Isaac Sim과 분리된 고성능 Headless-first 실행 코어

## 현재 상태

현재 기준 설계는 `Architecture v2`입니다. v1의 Canonical Model, 결정론적 DES, Headless-first 원칙을 유지하면서 Job_Tasks의 OHT 메인 에뮬레이터, OCS, OCS Replay를 **Legacy Reference System**으로 분석했습니다.

해당 프로그램의 프로세스 경계나 내부 구조를 Sim_Core에 계승하지 않고, 분석에서 발견된 유용한 요구사항만 다음과 같은 범용 기능으로 재설계했습니다.

- 풍부한 `VehicleRuntimeState`와 단계별 movement fidelity
- 교체 가능한 Policy Architecture
- Event Timeline 기반 Replay와 Time Travel Debugging
- Deterministic Rerun과 Run Comparison
- 운영 데이터 기반 Scenario Reconstruction
- 범용 Source Identity / provenance 추적

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
10. 권한이 불명확한 코드, 바이너리, UI 자산은 제품 코드에 포함하지 않습니다.

## 계획된 저장소 구조

```text
Sim_Core/
├── apps/                    # CLI와 서비스 실행 진입점
├── bindings/                # Python/Isaac Sim 연동 경계
├── include/sim_core/        # 공개 C++ API
├── schemas/                 # facility, scenario, runtime, event, result schema
├── src/
│   ├── application/         # use case와 run orchestration
│   ├── domain/              # OHT, Job, Network, Resource 모델
│   ├── kernel/              # 시간, event queue, scheduler, RNG
│   ├── modules/             # routing, dispatch, mobility, traffic, energy, deadlock
│   ├── observability/       # timeline, replay, snapshot, comparison, analytics
│   ├── ports/               # importer, store, observer, integration 인터페이스
│   └── adapters/            # JSON/CSV 및 권한 확인된 외부 포맷 adapter
└── tests/                   # unit, contract, golden, regression, performance
```

구조는 구현 커밋에서 필요한 디렉터리부터 순차적으로 생성합니다.

## 기준 분석 자료

[AutoMod OHT 종합 정적분석 보고서](AutoMod_OHT_Materials_Comprehensive_Analysis_2026-07-15.docx)와 권한이 확인된 Legacy OHT 관련 자료는 요구사항과 실패 사례를 식별하는 참고 자료입니다. 해당 자료의 상용 코드나 런타임 구현을 제품 코드로 복사하지 않으며, 원본 사례는 사용 권한과 보안 검토를 통과한 정제 fixture만 회귀시험에 사용합니다.
