
Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c wmic process WHERE NAME='python.exe' list full 2>NUL | find /I ""PowerManager.py"" & if %errorlevel%==1 (python PowerManager.py)", 0, False
Set objShell = Nothing