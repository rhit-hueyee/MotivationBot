@echo off
setlocal enabledelayedexpansion

REM Activate virtual environment
call env\Scripts\activate

REM Run linter
echo Running flake8...
flake8 .\src .\tests > flake8_report.txt 2>&1

REM Initialize error counters
set E=0
set W=0
set F=0
set C=0
set ErrCount=0

REM Read flake8 output and count error types
for /f "tokens=4 delims=: " %%a in (flake8_report.txt) do (
    set "code=%%a"
    set "category=!code:~0,1!"

    if "!category!"=="E" set /a E+=1
    if "!category!"=="W" set /a W+=1
    if "!category!"=="F" set /a F+=1
    if "!category!"=="C" set /a C+=1
)

set /a ErrCount=%E% + %W% + %F% + %C%

if %ErrCount% neq 0 (
    REM Display the results
    type flake8_report.txt
    echo Errors ^(^E^): %E%
    echo Warnings ^(^W^): %W%
    echo PyFlakes issues ^(^F^): %F%
    echo McCabe complexity warnings ^(^C^): %C%
    echo Found %ErrCount% errors.
) else (
    echo No errors found.
)
echo.

REM Run tests
echo Running pytest...
pytest .\tests
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

echo Check completed successfully.

endlocal
