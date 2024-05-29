@echo off
setlocal

REM Activate virtual environment
call env\Scripts\activate

echo Starting the program...
python .\src\main.py

endlocal
