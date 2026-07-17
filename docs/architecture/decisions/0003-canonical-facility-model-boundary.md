# ADR-0003: Canonical Facility Model 경계

- 상태: Accepted
- 날짜: 2026-07-17

## Context

FAB 레이아웃은 CAD, OHT map, station/port 데이터, 시뮬레이션 모델 등 여러 형식과 시점으로 존재할 수 있습니다. 각 module이 원본 포맷을 직접 읽으면 ID, 단위, 연결성 판단과 버전 관리가 중복되고 source 변경이 runtime까지 전파됩니다.

## Decision

모든 원본은 Import Adapter를 통해 immutable `FacilityModelRevision`으로 변환합니다.

- Canonical Model은 Node, directed Edge, ControlPoint, Station, Zone, Parking, Charger, VehicleType을 표현합니다.
- geometry와 connectivity를 분리합니다.
- 원본 ID는 namespace와 source reference로 보존합니다.
- source SHA-256, importer version, 단위, 좌표계, diagnostic을 revision에 기록합니다.
- model과 scenario를 분리합니다.
- runtime은 원본 parser type이나 file handle을 참조하지 않습니다.
- 자동 보정은 명시된 transformation으로만 수행하고 결과 diff를 남깁니다.

## Consequences

### 장점

- importer가 바뀌어도 kernel과 domain module이 보호됩니다.
- 동일 layout에 여러 운영 scenario를 적용할 수 있습니다.
- source 시점 혼합과 ID 변환을 추적할 수 있습니다.
- validation과 model diff를 simulation 전에 수행할 수 있습니다.

### 비용

- 중립 schema와 migration policy를 유지해야 합니다.
- 원본 포맷의 모든 세부값을 즉시 표현하지 못할 수 있습니다.
- 큰 모델은 compile-time index와 compact runtime representation이 추가로 필요합니다.

## Rule

Canonical schema에 없는 원본 필드는 이름 없는 map에 무제한 저장하지 않습니다. 실제 domain 의미가 확인되면 versioned extension으로 승격하고, 미확인 값은 provenance payload에 격리합니다.
