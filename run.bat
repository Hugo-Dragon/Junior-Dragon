@echo off
echo 1. Run the bot
echo 2. Install packages
echo 3. Exit
choice /c 123 /n /m "Choice:"
:: Note - list ERRORLEVELS in decreasing order
IF ERRORLEVEL 3 GOTO optone
IF ERRORLEVEL 2 GOTO install
IF ERRORLEVEL 1 GOTO run

:run
echo Running Bot, Please wait...
echo Python Version:
python -version
echo `n
python app.py

:install
echo Installing Packages
python -m pip install -r requirements.txt
GOTO end

:optone
GOTO endx

:endx
exit

:end
pause
