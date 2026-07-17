# Sim_Core

Sim_Core는 FAB 물류, 특히 OHT 운영 정책을 실험하기 위한 **독립형 이산사건 시뮬레이션 코어**입니다.

이 저장소의 목표는 특정 상용 시뮬레이터를 복제하는 것이 아닙니다. 권한이 확인된 입력 자료와 공개 규격, 독립적으로 정의한 도메인 계약을 기반으로 다음 기능을 구현합니다.

- 레이아웃과 운영 데이터의 중립 모델 변환 및 검증
- 동일 입력과 시드에서 동일 결과를 만드는 결정론적 DES 커널
- OHT 라우팅, 배차, 이동 예약, 에너지, 교착 진단
- 실행 근거를 추적할 수 있는 이벤트 로그와 결과 지표
- 2D/3D 및 Isaac Sim과 분리된 헤드리스 실행 코어

## 현재 상태

현재 단계는 `Architecture v1`입니다. 구현에 앞서 시스템 경계, 모듈 책임, 데이터 계약, 재현성 원칙과 단계별 개발 순서를 확정했습니다.

- [Simulator Architecture v1](docs/architecture/SIM_CORE_ARCHITECTURE_V1.md)
- [ADR-0001: 독립 구현과 Clean-room 경계](docs/architecture/decisions/0001-independent-clean-room-boundary.md)
- [ADR-0002: 결정론적 DES와 정수 시간](docs/architecture/decisions/0002-deterministic-des-and-integer-time.md)
- [ADR-0003: Canonical Facility Model 경계](docs/architecture/decisions/0003-canonical-facility-model-boundary.md)
- [ADR-0004: C++20 헤드리스 코어](docs/architecture/decisions/0004-cpp20-headless-core.md)

## 핵심 설계 원칙

1. 원본 포맷은 Import Adapter 밖으로 새지 않습니다.
2. 시뮬레이션 결과의 기준은 UI나 3D가 아니라 헤드리스 코어입니다.
3. 모델 revision, 시나리오, seed, 엔진 버전이 같으면 이벤트 순서와 결과 hash가 같아야 합니다.
4. 차량 상태 변경과 자원 대기는 원인 event까지 설명할 수 있어야 합니다.
5. 이동 충실도는 단순 이동 시간부터 구역 제어까지 단계적으로 높입니다.
6. 권한이 불명확한 코드, 바이너리, UI 자산은 제품 코드에 포함하지 않습니다.

## 계획된 저장소 구조

```text
Sim_Core/
├── apps/                    # CLI와 향후 서비스 실행 진입점
├── bindings/                # Python/Isaac Sim 연동 경계
├── include/sim_core/        # 공개 C++ API
├── schemas/                 # Canonical model, scenario, result schema
├── src/
│   ├── application/         # use case와 run orchestration
│   ├── domain/              # OHT, Job, Network, Resource 모델
│   ├── kernel/              # 시간, event queue, scheduler, RNG
│   ├── modules/             # routing, dispatch, mobility, energy, deadlock
│   ├── ports/               # importer, store, observer 인터페이스
│   └── adapters/            # JSON/CSV 및 권한 확인된 원본 포맷 adapter
└── tests/                   # unit, contract, golden, regression
```

구조는 구현 커밋에서 필요한 디렉터리부터 순차적으로 생성합니다.

## 기준 분석 자료

[AutoMod OHT 종합 정적분석 보고서](AutoMod_OHT_Materials_Comprehensive_Analysis_2026-07-15.docx)는 요구사항과 실패 사례를 식별하는 참고 자료입니다. 해당 자료의 상용 코드나 런타임 구현을 제품 코드로 복사하지 않으며, 원본 사례는 사용 권한과 보안 검토를 통과한 정제 fixture만 회귀시험에 사용합니다.
