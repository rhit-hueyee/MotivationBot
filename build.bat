@echo off

REM Activate virtual environment
call venv\Scripts\activate

REM Run linter
echo Running flake8...
flake8 .\src > flake8_report.txt 2>&1
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

REM Run tests
echo Running pytest...
pytest .\src\tests
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

echo Build completed successfully.
