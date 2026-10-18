. (Join-Path $PSScriptRoot '_common.ps1')
Invoke-DocsPython -c 'import sys,struct,importlib.metadata; print("Python",sys.version.split()[0],"bits",struct.calcsize("P")*8); print("Zensical",importlib.metadata.version("zensical")); assert sys.version_info[:2] == (3,13); assert struct.calcsize("P")==8; assert importlib.metadata.version("zensical")=="0.0.71"'
Invoke-DocsPython (Join-Path $PSScriptRoot 'validate.py')
Write-Output 'Local scaffold check complete. Caddy, tunnel creation, public DNS, and startup tasks are outside D02.'
