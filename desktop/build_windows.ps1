$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$BuildDir = Join-Path $RepoRoot "build"
$CoreBinary = Join-Path $BuildDir "Release\sim-core.exe"
$SampleDir = Join-Path $RepoRoot "examples\cross_domain"
$AppIcon = Join-Path $RepoRoot "desktop\generated\sim_core_workbench.png"

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
& $Python -m pip install pillow

# Generate the dedicated Sim_Core icon used by the Windows executable.  The
# runtime window icon is drawn by english_ui_patch.py from the same design.
$env:QT_QPA_PLATFORM = "offscreen"
& $Python desktop\generate_app_icon.py
if ($LASTEXITCODE -ne 0 -or -not (Test-Path $AppIcon)) {
    throw "Application icon generation failed."
}

& $Python desktop\test_dxf_graph_converter.py
if ($LASTEXITCODE -ne 0) {
    throw "DXF graph converter tests failed."
}
& $Python desktop\test_cad_graph_facility.py
if ($LASTEXITCODE -ne 0) {
    throw "CAD graph Facility adapter tests failed."
}
& $Python desktop\test_vehicle_simulation_engine.py
if ($LASTEXITCODE -ne 0) {
    throw "Vehicle simulation engine tests failed."
}
& $Python desktop\test_vehicle_simulation_drawing1.py
if ($LASTEXITCODE -ne 0) {
    throw "Drawing1 vehicle simulation integration test failed."
}
& $Python desktop\test_vehicle_simulation_ui.py
if ($LASTEXITCODE -ne 0) {
    throw "Vehicle simulation Qt UI tests failed."
}
& $Python desktop\test_rail_file.py
if ($LASTEXITCODE -ne 0) {
    throw "Rail file adapter tests failed."
}
& $Python desktop\test_automod_pm_converter.py
if ($LASTEXITCODE -ne 0) {
    throw "AutoMod model.arc converter tests failed."
}
& $Python desktop\test_isaac_sim_exporter.py
if ($LASTEXITCODE -ne 0) {
    throw "NVIDIA Isaac Sim exporter tests failed."
}

cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release --parallel
ctest --test-dir build -C Release --output-on-failure

if (-not (Test-Path $CoreBinary)) {
    throw "Core binary not found: $CoreBinary"
}

$env:SIM_CORE_BIN = $CoreBinary
$env:QT_QPA_PLATFORM = "offscreen"
& $Python desktop\smoke_test.py
if ($LASTEXITCODE -ne 0) {
    throw "Native desktop smoke test failed."
}
& $Python desktop\graph_ui_smoke_test.py
if ($LASTEXITCODE -ne 0) {
    throw "Graph UI enhancement smoke test failed."
}

$PyInstallerArgs = @(
    "--noconfirm",
    "--clean",
    "--onefile",
    "--windowed",
    "--name", "Sim_Core_Flow_Workbench",
    "--icon", "$AppIcon",
    "--add-binary", "$CoreBinary;.",
    "--add-data", "$SampleDir;examples\cross_domain",
    "--collect-all", "ezdxf",
    "desktop\app_wrapper.py"
)

& $Python -m PyInstaller @PyInstallerArgs

Write-Host ""
Write-Host "Build complete:" -ForegroundColor Green
Write-Host (Join-Path $RepoRoot "dist\Sim_Core_Flow_Workbench.exe")
