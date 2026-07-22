# DXF → 방향성 Graph JSON 개발 기준

## 목적

FAB 레이아웃 DXF의 Rail geometry를 Sim_Core Workbench에서 직접 열고, 방향성 Graph JSON으로 변환한 뒤 2D 화면에서 확인할 수 있게 합니다.

기준 구현은 `Mega-Sim/Graph_Maker_CAD-dxf-_to_json`의 다음 파이프라인입니다.

1. DXF modelspace의 `LINE`과 `ARC`를 선분으로 읽기
2. 좌표를 소수점 3자리로 반올림해 Node 중복 제거
3. 선분 endpoint를 Edge로 연결
4. 이전 진행 벡터와 후보 Edge의 내적이 가장 큰 경로를 이어 방향 추정
5. `nodes`와 `edges[{start, end, dir}]`를 JSON으로 저장

## Workbench 보강 사항

참조 구현의 결과 형식과 Thread/dot-product 방향 규칙은 유지하면서 실제 UI 사용에 필요한 항목을 보강했습니다.

- 첫 Edge와 연결되지 않은 geometry도 같은 방향 Thread 계산을 다시 시작
- 모든 Edge의 `dir`가 `[fromNode, toNode]` 형태인지 검증
- Rail Layer 선택, ARC 분할 수, 좌표 반올림 자릿수 설정
- 원본 파일 SHA-256, 선택 Layer, Entity 수, Component 수를 metadata에 기록
- 파일 선택 즉시 메모리 변환 및 방향 화살표 포함 2D 표시
- 별도 저장 버튼으로 Graph JSON 생성
- 독립 CLI와 자동 단위 시험 제공

참조 샘플 `Drawing1.dxf` 비교 결과는 다음과 같습니다.

| 항목 | 참조 구현 | Workbench 구현 |
|---|---:|---:|
| Nodes | 220 | 220 |
| Edges | 214 | 214 |
| Node 좌표·Edge endpoint | 기준 | 동일 |
| `dir: null` Edge | 170 | 0 |
| 연결 Components | 미기록 | 8 |

## 출력 계약

```json
{
  "format_version": "1.0.0",
  "metadata": {
    "coordinate_unit": "millimeter",
    "selected_layers": ["OHT_RAIL_CENTER"],
    "direction_inference": {
      "method": "thread-continuity-dot-product",
      "authoritative": false,
      "review_required": true
    }
  },
  "nodes": [[0.0, 0.0], [1000.0, 0.0]],
  "edges": [
    {"start": 0, "end": 1, "dir": [0, 1]}
  ]
}
```

`nodes`와 `edges`는 참조 저장소와 호환되는 핵심 payload입니다. `metadata`는 변환 재현성과 검토를 위한 정보이며 절대 경로는 기록하지 않습니다.

## 현재 경계

- 지원 geometry는 참조 구현과 동일하게 `LINE`, `ARC`입니다.
- ARC는 참조 구현과 동일하게 시작각에서 끝각까지의 signed angle 차이를 지정 분할 수로 나눕니다.
- 선이 화면상 교차하더라도 endpoint가 같은 좌표가 아니면 자동 교차 Node를 만들지 않습니다.
- 방향은 geometry 기반 추정이며 운행 방향의 근거 데이터가 아닙니다.
- Station, EQ Port, Control Point 의미 부여와 Canonical Facility Model 생성은 별도 Adapter 단계입니다.

이 경계를 UI의 결과 설명과 JSON metadata에 함께 표시해, 추정 Graph가 검토 없이 Simulation Truth로 사용되지 않도록 합니다.
