:: Call the deactivate, to 'turn off' the virtual env in this command prompt
call .\.venv\Scripts\deactivate.bat

:: Reset the PYTHONPATH variable to what it was before
if defined _OLD_PYTHONPATH (
    set "PYTHONPATH=%_OLD_PYTHONPATH%"
    set _OLD_PYTHONPATH=
)

rmdir .venv /S /Q