$ErrorActionPreference = 'Stop'
$docsRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$docsPython = Join-Path $docsRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $docsPython)) { throw 'Missing project virtual environment. Run Initialize-Environment.ps1 with an explicit Python interpreter.' }
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:PYTHONUTF8 = '1'
function Invoke-DocsPython {
    param([Parameter(ValueFromRemainingArguments=$true)][string[]]$PythonArguments)
    & $docsPython -B @PythonArguments
    if ($LASTEXITCODE -ne 0) { throw "Documentation command failed with exit code $LASTEXITCODE." }
}
