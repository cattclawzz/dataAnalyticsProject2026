cd /d "%~dp0source"

start "" /d "%cd%" py app.py
timeout /t 2 >nul
start "" http://127.0.0.1:5000/