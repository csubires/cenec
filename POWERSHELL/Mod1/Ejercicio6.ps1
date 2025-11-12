
New-Item -Path .\Reportes -ItemType Directory
New-Item -Path .\Reportes\resumen.txt -ItemType File
New-Item -Path .\Backup -ItemType Directory
New-Item -Path .\Final -ItemType Directory

Copy-Item .\Reportes\resumen.txt .\Backup
Move-Item .\Reportes\resumen.txt .\Final

Remove-Item .\Final\resumen.txt -Recurse -Force
Remove-Item .\Final -Recurse -Force

Get-ChildItem -Recurse | Where-Object { $_.Length -gt 1MB }
Get-Process | Where-Object { $_.CPU -gt 100 }

Get-Process
Stop-Process
Start-Process

Stop-Process -id  12064
Stop-Process -name notepad -confirm
Start-Process notepad
