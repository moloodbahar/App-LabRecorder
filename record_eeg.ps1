# Set directory to where LabRecorderCLI.exe is
Set-Location C:\Synsensus\App-LabRecorder\build\Release

# Get timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$outputFile = "eeg_${timestamp}.xdf"

# Start recording
Write-Host "Recording to: $outputFile"
.\LabRecorderCLI.exe $outputFile 'name=\"TestStream\"' 