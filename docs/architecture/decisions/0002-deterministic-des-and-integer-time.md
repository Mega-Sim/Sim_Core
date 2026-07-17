# ADR-0002: 결정론적 DES와 정수 Simulation Time

- 상태: Accepted
- 날짜: 2026-07-17

## Context

OHT 시뮬레이션에서는 같은 시각의 이동 완료, resource release, dispatch가 어떤 순서로 처리되는지에 따라 배차, 대기와 교착이 달라집니다. 부동소수점 시간과 비결정적 container iteration은 동일 입력의 재현을 방해합니다.

## Decision

- runtime 시간은 `int64` microsecond tick을 사용합니다.
- 외부 시간은 compile 단계에서 versioned rounding policy로 변환합니다.
- event 정렬 key는 `(sim_time_us, priority, insertion_sequence)`입니다.
- event-loop thread 하나만 authoritative state를 변경합니다.
- event 취소는 generation/tombstone을 사용합니다.
- named RNG stream을 사용하고 algorithm/version을 run manifest에 기록합니다.
- 동일 run fingerprint의 event trace hash가 같아야 합니다.
- 과거 event 예약과 무한 zero-delay loop를 runtime 오류로 처리합니다.

## Consequences

### 장점

- 실패와 교착을 동일한 순서로 재현할 수 있습니다.
- 비교 test가 최종 지표뿐 아니라 첫 divergence event를 찾을 수 있습니다.
- Viewer 속도와 host wall clock이 simulation 결과에 영향을 주지 않습니다.

### 비용

- 외부 실수 시간을 tick으로 바꾸는 rounding 규칙을 관리해야 합니다.
- single-writer 구조가 장기적으로 병목이 될 수 있습니다.
- parallel 계산 결과를 canonical order로 merge해야 합니다.

## Revisit condition

고정 benchmark에서 event-loop가 목표 성능을 충족하지 못하고 profiling으로 mutation serialization이 병목임이 증명될 때만 parallel DES를 재검토합니다.
