; minimal inno script
[Setup]
AppName=ZRom Cleaner
AppVersion=0.3.0
DefaultDirName={pf}\ZRom Cleaner
OutputBaseFilename=ZRomCleanerSetup
SetupIconFile=assets\zrom.ico
[Files]
Source: "dist\ZRomCleaner.exe"; DestDir: "{app}"
[Icons]
Name: "{group}\ZRom Cleaner"; Filename: "{app}\ZRomCleaner.exe"
