. (Join-Path $PSScriptRoot '_common.ps1')
Invoke-DocsPython (Join-Path $PSScriptRoot 'render_registry.py') --check
Invoke-DocsPython (Join-Path $PSScriptRoot 'validate.py') --site (Join-Path $docsRoot '.build\site') --check-freshness --report (Join-Path $docsRoot '.build\validation.json')
