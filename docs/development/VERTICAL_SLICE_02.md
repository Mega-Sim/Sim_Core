# Sim_Core 2차 Cross-Domain Validation Vertical Slice

| 항목 | 값 |
|---|---|
| 개발 버전 | `0.2.0` |
| 기준 아키텍처 | `Architecture v5` |
| 브랜치 기준점 | `1f8db9f152f9ecef674a0f59fd57417e2b49f0ba` |
| 실행 형태 | C++20 정적 라이브러리와 `sim-core analyze` Headless CLI |
| 입력 | Canonical Facility JSON, Scenario JSON, 선택적 From-To CSV |
| 출력 | versioned Cross-Domain JSON Report |

## 1. 개발 목적

2차 개발은 시뮬레이션을 실행한 뒤 오류를 찾는 방식이 아니라, 서로 다른 engineering domain 입력이 하나의 Canonical Model에서 일관되는지를 실행 전에 확인하는 품질 게이트를 구현합니다.

1차 DES Vertical Slice는 회귀 기준으로 유지합니다. 2차 분석 계층은 Simulation Runtime을 직접 변경하지 않으며, 통과한 Canonical revision과 Scenario만 이후 DES·Flow Intelligence·ROI Reduction으로 전달합니다.

```text
Facility / EQ / Control / Resource / From-To
                    |
                    v
         Canonical JSON Loader 1.0/1.1
                    |
                    v
         Structural Validator
                    |
                    v
       Cross-Domain Validator 0.2
          |         |         |
          v         v         v
      Identity   Geometry   Demand/Route
          \         |         /
           Cross-Domain JSON Report
```

## 2. Canonical 계약 확장

Facility Schema `1.1.0`은 1차의 Node, Edge, Station에 다음 계약을 추가합니다.

| 계약 | 핵심 필드 | 목적 |
|---|---|---|
| `GeometryTransform` | source/target frame, rational scale, translation | source geometry 변환 이력 보존 |
| `ControlPoint` | attachment node, control type | merge/branch 등 제어 지점 표현 |
| `Zone` | node/edge membership, capacity | 교통 제어 구역 경계와 용량 |
| `Parking` | station, capacity, vehicle types | 대기 자원 검증 |
| `Charger` | station, capacity, vehicle types | 충전 자원 검증 |
| `VehicleType` | maximum speed, 3D dimensions | 차량 물리 계약 기준선 |
| `Station` 확장 | declared pose, handling capacity | EQ/rail pose와 From-To pressure 비교 |

Scenario Schema `1.1.0`은 다음 From-To 수요를 추가합니다.

```text
FromToDemand
  id
  from_station_id
  to_station_id
  expected_moves_per_hour
```

`1.0.0` 파일은 Loader에서 기존 필드를 그대로 유지하고 1.1 확장 collection을 빈 값으로 해석합니다. 따라서 최초 Golden Scenario를 변경하지 않고 회귀시험할 수 있습니다.

## 3. 실제 Content Hash

Facility `1.1.0`의 `content_hash`는 입력 JSON에서 `content_hash` 필드만 제외한 뒤 object key를 정렬하고 compact JSON으로 직렬화한 byte sequence의 SHA-256입니다. Array 순서는 모델 계약의 일부로 유지합니다.

```text
sha256:<64 lowercase hexadecimal characters>
```

Loader가 계산한 값과 선언 값이 다르면 `CONTENT_HASH_MISMATCH`로 실행 전에 차단합니다. SHA-256 구현은 외부 command나 플랫폼별 crypto API에 의존하지 않아 Headless 환경에서도 같은 결과를 만듭니다.

## 4. Cross-Domain Rule Set

| Rule ID | Severity | 검출 내용 |
|---|---|---|
| `CDV-IDENTITY-001` | ERROR | 서로 다른 entity type이 같은 Canonical ID 사용 |
| `CDV-IDENTITY-002` | ERROR | 하나의 source identity가 여러 Canonical entity에 매핑 |
| `CDV-PROVENANCE-001` | WARNING | source identity namespace에 source artifact 없음 |
| `CDV-GEOMETRY-001` | ERROR | source namespace의 geometry transform 중복 |
| `CDV-GEOMETRY-002` | ERROR | transform target과 canonical frame 불일치 |
| `CDV-GEOMETRY-003` | ERROR | source/canonical frame이 다른데 transform 없음 |
| `CDV-GEOMETRY-004` | ERROR | station pose와 attachment node가 1,000 um 초과 불일치 |
| `CDV-DEMAND-001` | ERROR | From-To endpoint station 없음 |
| `CDV-DEMAND-002` | ERROR | 빈도 값이 0 이하 또는 비정상 수치 |
| `CDV-DEMAND-003` | ERROR | 방향성 rail graph에서 From-To pair 도달 불가 |
| `CDV-CAPACITY-001` | WARNING | station 예상 입출고 pressure가 선언 capacity 초과 |
| `CDV-REVISION-001` | ERROR | 서로 다른 model lineage 비교 |
| `CDV-REVISION-002` | ERROR | 같은 revision ID가 서로 다른 content hash 사용 |
| `CDV-REVISION-003` | WARNING | 이전 source identity가 새 revision에서 사라짐 |
| `CDV-REVISION-004` | ERROR | source identity가 다른 Canonical entity로 remap |
| `CDV-REVISION-005` | INFO | 동일 Canonical node의 좌표 이동 |

각 진단은 `diagnostic_id`, severity, category, `rule_id`, source/canonical entity, message, evidence, suggested action을 함께 기록합니다. 자동 수정은 수행하지 않습니다.

## 5. From-To Route Observation

정상 From-To row는 진단 없이 다음 관측값으로 변환됩니다.

- 선택된 방향성 edge path
- 총 route distance
- edge speed limit 기반 자유주행시간
- expected moves/hour

동일 cost 경로의 선택은 1차 `DijkstraRouter`의 edge ID tie-break 규칙을 그대로 사용하므로 반복 실행 결과가 동일합니다.

합성 예제 결과:

| Demand | Route | Distance | Free-flow time | Frequency |
|---|---|---:|---:|---:|
| `OD-A-C` | `E-A-B → E-B-C` | 30,000,000 um | 15,000,000 us | 40/hour |

## 6. 중립 From-To CSV Adapter

CSV Adapter는 특정 상용 제품 포맷을 복제하지 않는 최소 중립 계약입니다.

```csv
id,from_station_id,to_station_id,expected_moves_per_hour
OD-A-C,ST-A,ST-C,40
```

- UTF-8 BOM과 CRLF 지원
- quoted field와 escaped quote 지원
- 필수 header, 중복 header, column count, 수치 형식 검증
- 원본 파일을 제품 코드나 fixture에 포함하지 않고 권한이 확인된 정제 입력만 사용

## 7. CLI

```bash
sim-core analyze \
  --facility FACILITY.json \
  --scenario SCENARIO.json \
  [--from-to-csv FROM_TO.csv] \
  [--baseline-facility BASELINE.json] \
  [--output REPORT.json]
```

- `--from-to-csv`: Scenario JSON의 From-To collection을 CSV 입력으로 교체
- `--baseline-facility`: 현재 모델과 source identity/content/geometry revision 비교
- `--output`: JSON report 저장. 생략하면 stdout 출력
- 종료 코드 `0`: ERROR 없음
- 종료 코드 `4`: Cross-Domain ERROR 존재
- 구조/JSON/실행 인자 오류는 기존 CLI와 동일하게 종료 코드 `2`

## 8. 자동 검증 결과

자동시험은 1차 7개 회귀시험과 2차 5개 시험을 함께 실행합니다.

- SHA-256 공식 `abc` test vector
- Facility 1.1 실제 content hash 일치·불일치
- 1.0 Facility/Scenario 하위 호환
- From-To CSV Import
- From-To route/distance/time 결정론
- Cross-Domain report byte-level 반복 일치
- source identity 충돌과 station pose 불일치
- source/canonical frame 차이의 transform 누락과 From-To 도달 불가
- station capacity pressure warning
- revision ID/hash 불변성 위반
- source identity remap
- 1차 DES Golden trace hash와 run fingerprint 불변

현재 검증 결과는 `12/12 tests passed`입니다.

## 9. 이번 범위에서 제외한 항목

- CAD/DXF, 실제 EQ List, OCS/PDS 운영 로그 Adapter
- 실제 고객/설비 데이터 fixture
- Flow allocation과 복수 후보 route share
- edge/zone capacity flow model
- Bottleneck score와 Heatmap
- ROI Selection과 Model Reduction
- UI와 Digital Twin Overlay

다음 개발 단위는 Architecture v5의 `A3 Flow Intelligence`입니다. 2차에서 생성한 `demand_routes`와 capacity warning을 입력으로 edge frequency, route concentration, merge pressure, capacity margin을 계산하는 것이 기준입니다.
