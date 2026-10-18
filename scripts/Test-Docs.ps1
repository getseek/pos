. (Join-Path $PSScriptRoot '_common.ps1')
Invoke-DocsPython -m unittest discover -s (Join-Path $docsRoot 'tests') -v
