cd %CD%/src/
python -m venv venv
CALL venv\Scripts\activate.bat
set FLASK_APP=app.py
set FLASK_ENV=development
flask run