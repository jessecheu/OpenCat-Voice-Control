
Using Python Virtual Environments: 

Create a virtual environment by: 
1) running `python -m venv .env` or whatever python virtual environment you want to use
2) Run `source ./.env/Scripts/activate` in git bash or `./.env/Scripts/activate.bat` for windows.
3) Run pip install -r requirements.txt
4) Check all the requirements are installed by running `pip list` 


For updating the resources file:
run `pyside6-rcc resources.qrc -o resources_rc.py`

For updating the .ui files:
`pyside6-uic index.ui > ui_index.py`