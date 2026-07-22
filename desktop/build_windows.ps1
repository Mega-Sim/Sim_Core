$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$BuildDir = Join-Path $RepoRoot "build"
$CoreBinary = Join-Path $BuildDir "Release\sim-core.exe"
$SampleDir = Join-Path $RepoRoot "examples\cross_domain"

Set-Location $RepoRoot

$Python = if (Get-Command python -ErrorAction SilentlyContinue) {
    (Get-Command python).Source
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    (Get-Command py).Source
} else {
    throw "Python 3.12 was not found."
}

& $Python -m pip install --upgrade pip
& $Python -m pip install -r desktop\requirements.txt
& $Python desktop\test_dxf_graph_converter.py
if ($LASTEXITCODE -ne 0) {
    throw "DXF graph converter tests failed."
}
& $Python desktop\test_random_flow_analysis.py
if ($LASTEXITCODE -ne 0) {
    throw "Random From-To static analysis tests failed."
}

cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release --parallel
ctest --test-dir build -C Release --output-on-failure

if (-not (Test-Path $CoreBinary)) {
    throw "Core binary not found: $CoreBinary"
}

$env:SIM_CORE_BIN = $CoreBinary
$env:QT_QPA_PLATFORM = "offscreen"
& $Python desktop\random_flow_core_smoke_test.py
if ($LASTEXITCODE -ne 0) {
    throw "Random From-To C++ Core cross-check failed."
}
& $Python desktop\smoke_test.py
if ($LASTEXITCODE -ne 0) {
    throw "Native desktop smoke test failed."
}
& $Python desktop\graph_ui_smoke_test.py
if ($LASTEXITCODE -ne 0) {
    throw "Graph UI enhancement smoke test failed."
}
& $Python desktop\random_flow_ui_smoke_test.py
if ($LASTEXITCODE -ne 0) {
    throw "Random From-To heatmap UI smoke test failed."
}

$PyInstallerArgs = @(
    "--noconfirm",
    "--clean",
    "--onefile",
    "--windowed",
    "--name", "Sim_Core_Flow_Workbench",
    "--add-binary", "$CoreBinary;.",
    "--add-data", "$SampleDir;examples\cross_domain",
    "--collect-all", "ezdxf",
    "desktop\app_wrapper.py"
)

& $Python -m PyInstaller @PyInstallerArgs

Write-Host ""
Write-Host "Build complete:" -ForegroundColor Green
Write-Host (Join-Path $RepoRoot "dist\Sim_Core_Flow_Workbench.exe")
