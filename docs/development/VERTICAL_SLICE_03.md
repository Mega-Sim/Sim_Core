# Sim_Core 3차 Flow Intelligence Vertical Slice

| 항목 | 값 |
|---|---|
| 개발 버전 | `0.3.0` |
| 기준 아키텍처 | `Architecture v5` |
| 대응 로드맵 | `A3 Flow Intelligence` |
| 실행 형태 | C++20 정적 라이브러리와 `sim-core analyze` Headless CLI |
| 입력 | 2차에서 검증한 Canonical Facility, Scenario, From-To 수요 |
| 출력 | Cross-Domain JSON Report에 추가된 flow 관측 섹션 |

## 1. 개발 목적

2차 Cross-Domain Validation은 서로 다른 domain 입력이 하나의 Canonical Model에서 일관되는지 확인하고, 정상 From-To 수요를 `demand_routes` 관측값으로 변환했습니다.

3차 개발은 그 `demand_routes`를 입력으로 삼아 **어디에 부하가 집중되는지를 시뮬레이션 이전에 저비용으로 사전 탐색**합니다. Architecture v5 6장 `Flow / Frequency Intelligence`와 로드맵 `A3`가 요구하는 다음 지표를 계산합니다.

- edge frequency (edge expected traversals / hour)
- route concentration (edge별 flow share)
- merge pressure (합류 node 유입 압력)
- capacity margin (station capacity 대비 여유)

정적 분석은 동적 시뮬레이션을 대체하지 않습니다. 병목 후보와 관심 구간(ROI)을 좁히는 앞단 지능 계층이며, 여기서 만든 관측값은 이후 Bottleneck Intelligence와 ROI Reduction의 공통 입력이 됩니다.

```text
Cross-Domain Validator 0.2
            |
            v
      demand_routes (reachable From-To)
            |
            v
     Flow Intelligence 0.3
      |        |        |
      v        v        v
  Edge Flow  Node Flow  Station Flow
      \        |        /
       Cross-Domain JSON Report (flow 섹션)
```

## 2. Flow 관측 계약

세 관측값을 report에 추가했습니다. 모두 진단(diagnostic)이 아니라 구조화된 관측값이며, 통과/실패 게이트를 바꾸지 않습니다.

| 관측값 | 핵심 필드 | 의미 |
|---|---|---|
| `EdgeFlowObservation` | `expected_moves_per_hour`, `flow_share`, `contributing_demand_ids` | edge 빈도와 route 집중도 |
| `NodeFlowObservation` | `inflow_moves_per_hour`, `incoming_edge_count`, `merge_pressure` | 유입/유출과 합류 압력 |
| `StationFlowObservation` | `peak_moves_per_hour`, `capacity_margin_per_hour`, `utilization_ratio`, `over_capacity` | station 부하와 capacity 여유 |

## 3. 집계 규칙

- **Edge frequency**: `demand_routes`의 각 edge에 대해 해당 경로를 지나는 수요의 `expected_moves_per_hour`를 합산합니다. flow가 없는 edge는 관측값에 나타나지 않습니다.
- **Route concentration**: `flow_share`는 이 edge의 이동량을 전체 edge 이동량 합으로 나눈 값입니다. 특정 corridor에 부하가 몰릴수록 값이 커집니다.
- **Merge pressure**: flow를 싣고 한 node로 들어오는 서로 다른 edge가 둘 이상이면 그 node를 합류점으로 보고 총 유입량을 `merge_pressure`로 기록합니다. 유입 edge가 하나면 0입니다.
- **Capacity margin**: station별 유입/유출 중 큰 값(`peak_moves_per_hour`)을 선언 capacity와 비교해 여유량, 사용률, 초과 여부를 계산합니다. capacity가 선언되지 않은 station은 0으로 둡니다.

집계는 오직 도달 가능(reachable)한 From-To 수요에서만 파생됩니다. 도달 불가 수요는 2차에서 `CDV-DEMAND-003`으로 이미 걸러지므로 flow 계산에 들어가지 않습니다.

## 4. 합성 예제 결과

기존 `examples/cross_domain` 예제(`OD-A-C`, 40/hour, `E-A-B → E-B-C`)는 다음을 산출합니다.

| Edge | Moves/hour | Flow share |
|---|---:|---:|
| `E-A-B` | 40 | 0.5 |
| `E-B-C` | 40 | 0.5 |

| Station | Inbound | Outbound | Capacity | Margin |
|---|---:|---:|---:|---:|
| `ST-A` | 0 | 40 | 120 | 80 |
| `ST-C` | 40 | 0 | 120 | 80 |

단일 경로이므로 모든 node의 `merge_pressure`는 0입니다.

자동시험은 두 경로가 한 node로 합류하는 토폴로지를 in-memory로 구성해, 유입 edge 2개·`merge_pressure = 70`·합류 station capacity margin 50을 확인합니다.

## 5. 결정론

flow 집계는 정렬된 `demand_routes`와 `std::map` 기반 누적만 사용하므로 동일 입력에서 동일 결과를 만듭니다. `edge_flows`, `node_flows`, `station_flows`는 각각 id 기준으로 정렬해 출력하며, `to_json()`은 반복 실행 시 byte 단위로 동일합니다.

1차 DES Golden Scenario의 `trace_hash`와 `run_fingerprint`는 이번 변경으로 바뀌지 않습니다. flow 계층은 Simulation Runtime을 건드리지 않고 분석 report에만 추가되기 때문입니다.

## 6. CLI

CLI 명령은 2차와 동일합니다. `analyze`의 JSON report에 `edge_flows`, `node_flows`, `station_flows` 세 배열이 추가됩니다.

```bash
sim-core analyze \
  --facility examples/cross_domain/facility.json \
  --scenario examples/cross_domain/scenario.json \
  --from-to-csv examples/cross_domain/from_to.csv \
  --output cross-domain-report.json
```

## 7. 자동 검증 결과

1차·2차 회귀시험 12개에 flow 시험 2개를 더해 실행합니다.

- edge frequency·flow share·contributing demand 집계
- 미사용 edge 제외
- station 유입/유출과 capacity margin
- merge 토폴로지에서 유입 edge 수와 merge pressure

현재 검증 결과는 `14/14 tests passed`입니다.

## 8. 이번 범위에서 제외한 항목

- 복수 후보 route 간 flow allocation(현재는 단일 최단 경로 기준)
- edge/zone 물리 용량 기반 flow 상한 모델
- 시간대별 arrival process와 queue 시뮬레이션
- Bottleneck score 결합식과 Heatmap 시각화
- ROI Selection과 Model Reduction

다음 개발 단위는 Architecture v5의 `A5 Bottleneck Intelligence`입니다. 3차에서 만든 edge frequency, route concentration, merge pressure, capacity margin을 topology score와 결합해 병목 후보 점수와 원인 설명을 생성하는 것이 기준입니다.
