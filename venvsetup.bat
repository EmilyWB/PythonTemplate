@echo off

:: Setup our virtual env in this project. 
:: Requires virtualenv exe to be on the PATH variable.
call virtualenv .venv

:: Activate the virtual env in this command prompt instance, 
:: so when we call Python it will use the local executable in .venv
call .\.venv\Scripts\activate.bat

:: Running Python from the virtual env, we do not get the current
:: working directory as part of the PYTHONPATH. Add it here.
if not defined _OLD_PYTHONPATH (
    set "_OLD_PYTHONPATH=%PYTHONPATH%"
    set "PYTHONPATH=%cd%;%PYTHONPATH%"
)

:: Go ahead and install our packages in the virtual env
call python -m pip install -r requirements.txt
