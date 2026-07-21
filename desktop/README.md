# Sim_Core Native Desktop Workbench

웹 서버나 HTTP 통신을 사용하지 않는 Windows 데스크톱 UI입니다. Qt 위젯으로 직접 화면을 그리고 `QProcess`로 C++ `sim-core.exe`를 호출합니다.

## 가장 쉬운 사용법

GitHub Actions의 `Sim_Core Native Desktop - Windows EXE` 실행 결과에서 `Sim_Core_Flow_Workbench-windows-x64` Artifact를 내려받아 압축을 풉니다.

```text
Sim_Core_Flow_Workbench.exe
```

위 파일을 더블클릭하면 됩니다. 별도의 Python, CMake 설치나 웹 브라우저가 필요하지 않습니다. 패키지 안에는 현재 브랜치에서 빌드한 `sim-core.exe`와 Cross-Domain 샘플이 포함됩니다.

## 개발 중 직접 실행

Python이 설치된 Windows에서:

```powershell
py -m pip install -r desktop\requirements.txt
py desktop\app.py
```

Core 기능까지 연결하려면 먼저 C++ Core를 빌드합니다.

```powershell
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release
py desktop\app.py
```

## 단일 EXE 직접 생성

Visual Studio 2022 C++ Build Tools, CMake, Python이 설치된 Windows PowerShell에서:

```powershell
powershell -ExecutionPolicy Bypass -File desktop\build_windows.ps1
```

결과:

```text
dist\Sim_Core_Flow_Workbench.exe
```

## 구현 경계

| 기능 | 상태 |
|---|---|
| Facility/Scenario/From-To 파일 선택 | 네이티브 구현 |
| Canonical Network 2D 표시 | 네이티브 구현 |
| `sim-core validate` | 실제 Core 연결 |
| `sim-core analyze` | 실제 Core 연결 |
| `sim-core run` | 실제 Core 연결 |
| CAD Import | 계약 생성 UI, 변환 엔진 미연결 |
| Bottleneck/ROI/Policy A-B/Digital Twin | 프로토타입 계약, Core 미연결 |

실행 결과는 `%USERPROFILE%\Documents\Sim_Core\Runs` 아래에 실행별로 저장됩니다.
