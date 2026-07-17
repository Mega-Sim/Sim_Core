# ADR-0004: C++20 Headless Core와 연동 경계

- 상태: Accepted
- 날짜: 2026-07-17

## Context

목표 workload는 수천 개 edge, 수백 대 차량, 장시간 event 실행과 반복 정책 실험을 포함합니다. 동시에 Isaac Sim 연동과 Python 기반 분석 편의성이 필요하지만, 3D runtime과 Python 실행 환경이 core의 결정론과 배포를 지배해서는 안 됩니다.

## Decision

- simulation core와 OHT domain module은 C++20으로 구현합니다.
- build는 CMake 기반 out-of-source 방식을 사용합니다.
- kernel hot path는 외부 framework 의존을 최소화합니다.
- 첫 배포 단위는 UI가 없는 CLI executable과 core library입니다.
- Python과 Isaac Sim은 versioned binding 또는 out-of-process adapter로 연결합니다.
- 외부 consumer는 facility snapshot과 timestamped state stream을 읽으며 core state를 직접 변경하지 않습니다.
- domain schema와 event/result 계약은 언어와 독립적으로 versioning합니다.

## Consequences

### 장점

- 대규모 반복 실행의 성능 여유와 메모리 제어가 좋습니다.
- Python/3D 환경 없이 core test와 batch 실행이 가능합니다.
- 시스템 SW 도구와 정적 분석, sanitizer를 활용하기 쉽습니다.

### 비용

- Python 단독 prototype보다 초기 scaffolding이 큽니다.
- binding과 ABI 경계를 별도로 관리해야 합니다.
- dependency와 compiler matrix를 CI에서 검증해야 합니다.

## Constraints

- public ABI를 초기에 넓히지 않습니다.
- Python object를 kernel event payload로 저장하지 않습니다.
- Viewer callback이 event-loop thread를 block하지 않도록 buffer 또는 observer adapter를 둡니다.
- 구체 library 선택은 dependency review와 최소 prototype 후 별도 ADR로 기록합니다.
