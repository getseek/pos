. (Join-Path $PSScriptRoot '_common.ps1')
Invoke-DocsPython (Join-Path $PSScriptRoot 'manage.py') build
