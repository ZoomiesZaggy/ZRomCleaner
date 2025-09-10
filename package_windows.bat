@echo off
set REL=release
set OUT=%REL%\ZRomCleaner_windows
set ZIP=%REL%\ZRomCleaner_windows.zip
if not exist %REL% mkdir %REL%
if exist %OUT% rmdir /s /q %OUT%
mkdir %OUT%
copy dist\ZRomCleaner.exe %OUT%\ >nul
copy README.md %OUT%\ >nul
copy VERSION.txt %OUT%\ >nul
mkdir %OUT%\assets
copy assets\zrom.ico %OUT%\assets\ >nul
powershell -NoProfile -Command "Compress-Archive -Path '%OUT%\*' -DestinationPath '%ZIP%' -Force"
echo done
