Get-ChildItem -Recurse -Filter "*.ui" | ForEach-Object {
    $BaseName = $_.BaseName
    $DirName = $_.Directory
    Write-Host  $BaseName
    pyside6-uic.exe $_.FullName -o "$DirName/AutoGen_$BaseName.py"
}

