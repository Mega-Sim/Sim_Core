# ADR-0001: 독립 구현과 Clean-room 경계

- 상태: Accepted
- 날짜: 2026-07-17

## Context

기준 보고서는 상용 시뮬레이션 모델, 생성 산출물, OHT 도구와 결과를 분석해 독립 시뮬레이터에 필요한 도메인 요구사항을 정리합니다. 일부 자료에는 기밀·복제 제한 표기와 혼합된 제3자 구성요소가 있으며, 상용 runtime의 핵심 구현은 제공 자료에 존재하지 않습니다.

## Decision

Sim_Core는 관찰 가능한 데이터 의미와 독립 사양을 기반으로 새로 구현합니다.

- 상용 실행기, DLL, 생성 C, UI 자산, 내부 명칭을 제품 코드로 복사하지 않습니다.
- 원본 분석 자료는 요구사항 탐색과 검증 현상 정의에만 사용합니다.
- 구현 코드의 API, type, algorithm은 Sim_Core가 독립적으로 정의합니다.
- 원본 사례를 test fixture로 사용할 때는 권한 확인, secret 제거, 최소화, provenance 기록을 거칩니다.
- 공개 규격 또는 권한이 확인된 포맷만 production importer로 활성화합니다.
- 상용 제품과 비교가 필요하면 통제된 입력/출력 black-box test로 수행하고 관찰 조건을 기록합니다.

## Consequences

### 장점

- 법적·보안 위험과 특정 vendor 종속을 줄입니다.
- 핵심 engine의 동작과 제한을 스스로 설명할 수 있습니다.
- 여러 원본 포맷에 공통인 OHT domain model을 만들 수 있습니다.

### 비용

- 상용 runtime과 초기 수치가 다를 수 있습니다.
- 이동, 충돌, 통계 경계를 독립 실험으로 calibration해야 합니다.
- 자료 사용 권한이 불명확하면 adapter와 fixture 개발이 지연될 수 있습니다.

## Enforcement

- 모든 importer는 `source_kind`, `source_hash`, `importer_version`을 기록합니다.
- PR review checklist에 원본 코드/자산 복사 여부와 fixture 권한을 포함합니다.
- 저장소 secret scanning과 binary allowlist를 적용합니다.
- 독립 구현 판단이 어려운 변경은 merge 전에 별도 검토합니다.
