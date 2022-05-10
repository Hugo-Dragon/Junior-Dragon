@echo off
echo Welcome to hugocoding, this batch file is edit by KL AE#2160
echo What do you want to do
choice /cs /c rie /m Please choose an option. r - Run the bot `ni - Install packages + Run the bot`ne - `Exit
IF %ERRORLEVEL% === 2 goto x
IF %ERRORLEVEL% === 1 goto y
IF %ERRORLEVEL% === 3 exit
:y
echo 正在下載需要的套件 (Also installing optional packages)
python -m pip install -r requirements.txt
echo 正在開始運行機器人,請稍後...
echo Python Version:
python -version
echo `n
python app.py

:x
echo 正在開始運行機器人,請稍後...
echo Python Version:
python -version
echo `n
python app.py
