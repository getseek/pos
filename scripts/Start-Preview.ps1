. (Join-Path $PSScriptRoot '_common.ps1')
& (Join-Path $PSScriptRoot 'Validate-Docs.ps1')
$previewStatePath=Join-Path $docsRoot '.build\preview-session.json'
if(Test-Path -LiteralPath $previewStatePath){
    $existingSession=Get-Content -LiteralPath $previewStatePath -Raw|ConvertFrom-Json
    if(Get-Process -Id $existingSession.supervisor_pid -ErrorAction SilentlyContinue){throw 'A recorded preview process still exists. Inspect or stop it before starting another.'}
}
$previewProbe=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,18181)
try{$previewProbe.ExclusiveAddressUse=$true;$previewProbe.Start()}finally{$previewProbe.Stop()}
$previewScript=Join-Path $PSScriptRoot 'manage.py'
$previewProcess=Start-Process -FilePath $docsPython -ArgumentList @('-B',('"'+$previewScript+'"'),'preview') -WorkingDirectory $docsRoot -WindowStyle Hidden -RedirectStandardOutput (Join-Path $docsRoot '.build\preview.stdout.log') -RedirectStandardError (Join-Path $docsRoot '.build\preview.stderr.log') -PassThru
$previewSession=[ordered]@{supervisor_pid=$previewProcess.Id;supervisor_start_ticks=$previewProcess.StartTime.ToUniversalTime().Ticks;project_root=$docsRoot;script=$previewScript;url='http://127.0.0.1:18181/'}
$previewSession|ConvertTo-Json|Set-Content -LiteralPath $previewStatePath -Encoding utf8
Write-Output ('Started project-owned preview supervisor PID '+$previewProcess.Id+' at http://127.0.0.1:18181/. Read .build\preview.stderr.log if startup fails.')
