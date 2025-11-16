echo Dependency check
python check_deps.py
@echo off
if %errorlevel% neq 0 (
    echo InstallinП required modules...
    pip install keyboard
)

echo StartinП...
python main.py
pause