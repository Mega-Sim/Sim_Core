$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$BuildDir = Join-Path $RepoRoot "build"
$CoreBinary = Join-Path $BuildDir "Release\sim-core.exe"
$SampleDir = Join-Path $RepoRoot "examples\cross_domain"

Set-Location $RepoRoot

py -m pip install --upgrade pip
py -m pip install -r desktop\requirements.txt

cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release --parallel
ctest --test-dir build -C Release --output-on-failure

if (-not (Test-Path $CoreBinary)) {
    throw "Core binary not found: $CoreBinary"
}

$PyInstallerArgs = @(
    "--noconfirm",
    "--clean",
    "--onefile",
    "--windowed",
    "--name", "Sim_Core_Flow_Workbench",
    "--add-binary", "$CoreBinary;.",
    "--add-data", "$SampleDir;examples\cross_domain",
    "desktop\app.py"
)

py -m PyInstaller @PyInstallerArgs

Write-Host ""
Write-Host "Build complete:" -ForegroundColor Green
Write-Host (Join-Path $RepoRoot "dist\Sim_Core_Flow_Workbench.exe")
