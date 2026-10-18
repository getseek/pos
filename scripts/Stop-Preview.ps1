. (Join-Path $PSScriptRoot '_common.ps1')
$previewStatePath=Join-Path $docsRoot '.build\preview-session.json'
if(-not (Test-Path -LiteralPath $previewStatePath)){Write-Output 'No recorded project preview.';return}
$previewSession=Get-Content -LiteralPath $previewStatePath -Raw|ConvertFrom-Json
if($previewSession.project_root -ne $docsRoot){throw 'Preview record belongs to another project.'}
$previewSupervisor=Get-Process -Id $previewSession.supervisor_pid -ErrorAction SilentlyContinue
if(-not $previewSupervisor){Write-Output 'Recorded supervisor exited; no processes stopped.';return}
if($previewSupervisor.StartTime.ToUniversalTime().Ticks -ne $previewSession.supervisor_start_ticks){throw 'Preview PID was reused; refusing to stop it.'}
$supervisorDetails=Get-CimInstance Win32_Process -Filter "ProcessId=$($previewSession.supervisor_pid)"
if(-not $supervisorDetails.CommandLine.Contains($previewSession.script)){throw 'Supervisor identity mismatch; refusing to stop it.'}
$processSnapshot=@(Get-CimInstance Win32_Process)
$ownedPreviewProcesses=[Collections.Generic.List[object]]::new()
$ownedPreviewProcesses.Add($supervisorDetails)
for($processIndex=0;$processIndex -lt $ownedPreviewProcesses.Count;$processIndex++){
    $parentId=$ownedPreviewProcesses[$processIndex].ProcessId
    foreach($previewChild in @($processSnapshot|Where-Object {$_.ParentProcessId -eq $parentId})){
        if($previewChild.Name -eq 'conhost.exe' -and
           $previewChild.ExecutablePath -eq (Join-Path $env:WINDIR 'System32\conhost.exe')){
            # Windows owns this console host; let it exit with its client.
            # Do not issue a stop command to an OS console process.
            continue
        }
        # Windows venv launchers add a base-interpreter process at each level.
        # Validate the entire descendant tree before stopping any process.
        if($previewChild.Name -notmatch '^python(w)?\.exe$' -or
           -not $previewChild.CommandLine.Contains($docsRoot) -or
           (-not $previewChild.CommandLine.Contains($previewSession.script) -and
            -not $previewChild.CommandLine.Contains((Join-Path $docsRoot '.premium-preview.toml')))){
            throw 'Unexpected child process; no stop action taken.'
        }
        $ownedPreviewProcesses.Add($previewChild)
    }
}
for($processIndex=$ownedPreviewProcesses.Count-1;$processIndex -ge 0;$processIndex--){
    $ownedDetails=$ownedPreviewProcesses[$processIndex]
    $currentDetails=Get-CimInstance Win32_Process -Filter "ProcessId=$($ownedDetails.ProcessId)" -ErrorAction SilentlyContinue
    if($currentDetails){
        if($currentDetails.CreationDate -ne $ownedDetails.CreationDate){throw 'Descendant PID was reused; refusing to stop it.'}
        Stop-Process -Id $ownedDetails.ProcessId -ErrorAction SilentlyContinue
    }
}
Remove-Item -LiteralPath $previewStatePath
Write-Output 'Stopped only the recorded Premium documentation preview process tree.'
