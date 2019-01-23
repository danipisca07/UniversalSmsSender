@ECHO OFF
ECHO.
ECHO Universal Bulk SMS sender
ECHO.

pip3 install pipenv

pipenv install

pipenv run ui.py

PAUSE
CLS
EXIT