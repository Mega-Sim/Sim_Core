# Sim_Core 최초 개발 Vertical Slice

| 항목 | 값 |
|---|---|
| 개발 버전 | `0.1.0` |
| 기준 아키텍처 | `Architecture v5` |
| 언어/빌드 | C++20 / CMake 3.24+ |
| 실행 형태 | UI 없는 `sim-core` CLI와 `sim_core` 정적 라이브러리 |
| Golden Scenario | 단일 방향 직선 Network, OHT 1대, Job 1건 |

## 1. 개발 목적

첫 개발은 전체 FAB 기능을 한꺼번에 구현하는 단계가 아닙니다. Architecture v5의 긴 개발 경로에서 다음 세 가지가 실제 코드로 연결되는지를 먼저 증명합니다.

1. Canonical Model을 읽고 시뮬레이션 전에 잘못된 topology와 scenario를 차단할 수 있는가
2. 같은 입력에서 event 처리 순서와 결과가 반복 가능하게 고정되는가
3. 차량 1대와 Job 1건의 최소 OHT 흐름을 UI·OCS·Isaac Sim 없이 완주하고 Replay할 수 있는가

## 2. 구현 범위

### 2.1 Canonical Foundation

- Facility revision metadata와 source provenance
- micrometer 정수 좌표와 명시적 coordinate reference
- Node, `ONE_WAY` Edge, Station
- 원본 namespace/external ID를 보존하는 Source Identity
- Edge polyline과 endpoint, 선언 길이의 일관성 검증
- Facility와 Scenario 분리
- JSON Schema `1.0.0`

현재 runtime 공간 단위는 `micrometer`, 시간 단위는 `microsecond`입니다. F0 이동 완료 시각을 정수 연산으로 계산하기 위한 첫 runtime profile이며, 외부 Adapter는 입력 단위를 이 경계에서 변환해야 합니다.

### 2.2 Deterministic DES Kernel

Event 정렬 키는 다음과 같습니다.

```text
(simulation_time_us, priority, insertion_sequence)
```

Priority 숫자는 중앙 enum으로만 정의합니다. 과거 event 예약은 거부하며, 취소는 queue 내부 임의 삭제가 아니라 cancellation generation을 증가시키는 tombstone 방식입니다. 같은 timestamp에서 처리 가능한 event 수에도 상한을 둡니다.

### 2.3 OHT F0 흐름

```text
DISPATCH_REQUESTED
  -> VEHICLE_ARRIVED_PICKUP
  -> LOADING_COMPLETED
  -> VEHICLE_ARRIVED_DROPOFF
  -> UNLOADING_COMPLETED
```

Routing은 방향성 multigraph에서 자유주행시간을 cost로 사용합니다. 동일 cost가 나오면 edge path와 vehicle ID를 정렬 기준으로 사용해 선택 결과를 고정합니다.

F0에서는 edge 내부 연속 위치, 가감속, 충돌, block 점유를 계산하지 않습니다. Route의 거리와 speed limit으로 도착 완료 시각만 예약합니다.

### 2.4 Observability와 Replay

각 처리 event는 다음 상태를 JSONL 한 줄로 남깁니다.

- event ID, simulation time, priority, insertion sequence
- cause event와 correlation ID
- vehicle/job/station ID
- event 처리 후 Vehicle/Job 상태
- 해당 event가 사용한 route distance

Run Manifest에는 model revision, scenario, master seed, engine version, run fingerprint, event 수, 최종 simulation time, trace hash를 기록합니다.

`fnv1a64` trace hash는 동일 실행 비교용이며 보안 검증용 hash가 아닙니다. 원본 artifact provenance에는 별도로 SHA-256을 사용합니다.

Replay는 현재 JSONL만으로 Vehicle/Job 최종 상태와 완료 Job 수를 재구성하는 최소 구현입니다. Snapshot, 임의 시점 복원, first-divergence comparison은 후속 범위입니다.

## 3. Golden Scenario 결과

입력:

- `ST-START → ST-PICKUP`: 10 m, 2 m/s
- `ST-PICKUP → ST-DROPOFF`: 20 m, 2 m/s
- Loading: 2 s
- Unloading: 3 s

예상 event 시각:

| 순서 | Event | 시각 |
|---:|---|---:|
| 1 | `DISPATCH_REQUESTED` | 0 s |
| 2 | `VEHICLE_ARRIVED_PICKUP` | 5 s |
| 3 | `LOADING_COMPLETED` | 7 s |
| 4 | `VEHICLE_ARRIVED_DROPOFF` | 17 s |
| 5 | `UNLOADING_COMPLETED` | 20 s |

고정 결과:

- Run status: `COMPLETED`
- 처리 event: `5`
- 최종 시각: `20,000,000 us`
- Trace hash: `70240b9d9276d97c`
- Run fingerprint: `5004192c136cc90e`
- Replay 결과: `OHT-001=IDLE`, `JOB-001=COMPLETED`

## 4. 자동 검증 범위

- 음수·overflow Simulation Time 차단
- Event priority와 insertion sequence 순서
- 과거 event 예약 차단
- cancellation generation과 zero-delay guard
- Facility/Scenario 정상 검증
- duplicate canonical ID 검출
- 단방향 unreachable dropoff 사전 검출
- 방향성 Dijkstra 거리와 이동시간
- 동일 거리 Vehicle의 ID 기반 결정론적 Dispatch
- Vehicle/Job 전체 상태 전이
- 반복 실행 Trace/Manifest byte-level 동일성
- Trace Replay 최종 상태 재구성

## 5. 이번 범위에서 제외한 항목

- 실제 AutoMod, CAD, OCS, Emulator 포맷 Import Adapter
- OCS 통신 또는 실제 설비 제어
- F1 이상 edge/block 점유와 Traffic Control
- 연속 위치·속도·가감속
- 다중 Job의 운영 정책 고도화
- Deadlock, Energy, Charging
- Flow Intelligence, 병목 Heatmap, ROI Reduction
- USD/Omniverse/Isaac Sim Adapter

Legacy 프로그램은 실행 구조나 코드를 복제하지 않았고, 관찰 가능한 OHT 상태와 Replay 요구만 독립 계약으로 구현했습니다.

## 6. 다음 개발 기준

다음 브랜치는 현재 Vertical Slice를 유지하면서 Architecture v5의 순서에 맞춰 Canonical Foundation과 Cross-Domain Validation을 확장하는 것이 기준입니다.

1. ControlPoint, Zone, Parking, Charger, VehicleType schema 확장
2. Canonical content hash의 실제 계산과 schema migration
3. source ID 충돌·revision diff·geometry transformation 진단
4. From-To 수요와 unreachable pair 교차검증
5. 실제 사용 권한이 확인된 최소 Import Adapter와 정제 fixture

이후 Flow/Distance/Frequency 분석으로 넘어가며, 현재 DES Vertical Slice는 각 확장 단계의 회귀시험 기준으로 유지합니다.
