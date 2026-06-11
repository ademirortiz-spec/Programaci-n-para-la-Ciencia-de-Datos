<#
Instala las dependencias listadas en requirements.txt.
Uso recomendando (desde la raíz del repo):
  powershell -File src\Install\install_requirements.ps1

Opciones:
  -Requirements : ruta a requirements.txt (por defecto ../../requirements.txt desde este script)
  -VenvPath    : ruta del entorno virtual a crear/usar (por defecto .venv)
  -CreateVenv  : crear y usar el venv (por defecto true). Si se pasa -CreateVenv:$false instalará en el entorno activo.
#>
param(
    [string]$Requirements = "..\..\requirements.txt",
    [string]$VenvPath = ".venv",
    [bool]$CreateVenv = $true
)

Set-StrictMode -Version Latest

$reqFull = Resolve-Path -Path $Requirements -ErrorAction SilentlyContinue
if (-not $reqFull) {
    Write-Error "No se encontró requirements.txt en: $Requirements"
    exit 2
}

if ($CreateVenv) {
    if (-not (Test-Path $VenvPath)) {
        Write-Host "Creando entorno virtual en $VenvPath..."
        python -m venv $VenvPath
        if ($LASTEXITCODE -ne 0) { Write-Error "Fallo creando venv"; exit 3 }
    }
    Write-Host "Activando entorno virtual $VenvPath..."
    & "$VenvPath\Scripts\Activate.ps1"
    if ($LASTEXITCODE -ne 0) { Write-Error "Fallo al activar el venv"; exit 4 }
}

Write-Host "Actualizando pip..."
python -m pip install --upgrade pip --disable-pip-version-check
if ($LASTEXITCODE -ne 0) { Write-Error "Fallo actualizando pip"; exit 5 }

Write-Host "Instalando dependencias desde: $($reqFull.Path)"
python -m pip install -r "$($reqFull.Path)"
if ($LASTEXITCODE -ne 0) { Write-Error "Instalación fallida"; exit 6 }

Write-Host "Instalación completada correctamente." -ForegroundColor Green
exit 0
