# Sim_Core 실행 UI

UI 관련 작업은 `feature/1차-des-vertical-slice`를 기반으로 분기한 `agent/1차-des-demo-ui`에서 관리합니다.

## 권장: 실제 1차 DES Demo UI

Windows에서 저장소 루트의 `run_des_demo_ui.bat`를 실행합니다.

이 UI에서는 다음을 확인할 수 있습니다.

- C++20 Sim_Core 빌드
- 7개 핵심 테스트 실행
- `examples/single_line` 샘플 시뮬레이션 실행
- Event Trace 및 Replay 결과 확인

## 범용 실행 UI

저장소 루트의 `run_simple_ui.bat`를 실행하면 현재 체크아웃의 실행 명령을 직접 실행하고 stdout/stderr를 확인할 수 있습니다.

```bash
python tools/simple_runner_ui.py
```

`자동 찾기`는 빌드된 `sim-core` 또는 알려진 실행 진입점을 우선 탐색합니다.

## 브랜치 구조

```text
main
  └─ Architecture v5 설계

feature/1차-des-vertical-slice
  └─ 1차 DES Vertical Slice 구현
       └─ agent/1차-des-demo-ui
            ├─ 실제 DES Demo UI
            └─ 범용 실행/점검 UI
```

UI 변경은 `main`이 아니라 `agent/1차-des-demo-ui`에서 진행합니다.
