param([Parameter(Mandatory=$true)][string]$PythonPath)
$ErrorActionPreference='Stop'
$docsRoot=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$docsEnvironment=Join-Path $docsRoot '.venv'
if(Test-Path -LiteralPath $docsEnvironment){throw 'Virtual environment already exists. Inspect it instead of replacing it.'}
$interpreterVersion=& $PythonPath -B -c 'import sys; print(str(sys.version_info.major)+"."+str(sys.version_info.minor))'
if($LASTEXITCODE -ne 0 -or $interpreterVersion -ne '3.13'){throw 'The current hash lock targets CPython 3.13 Windows x64.'}
& $PythonPath -m venv $docsEnvironment
if($LASTEXITCODE -ne 0){throw 'Virtual environment creation failed.'}
$docsPython=Join-Path $docsEnvironment 'Scripts\python.exe'
& $docsPython -m pip --isolated install --index-url https://pypi.org/simple --disable-pip-version-check --cache-dir (Join-Path $docsRoot '.build\pip-cache') --require-hashes -r (Join-Path $docsRoot 'requirements.lock')
if($LASTEXITCODE -ne 0){throw 'Locked dependency installation failed.'}
