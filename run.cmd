@echo off
python pw.py
if errorlevel 1 exit /b 1

python compare.py "base.html" "remote.html"
pause