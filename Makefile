venv/bin/activate.bat: requirements.txt
	python3 -m venv venv
	./venv/Scripts/pip.exe install -r requirements.txt

dev:
	python3 -m venv venv
	./venv/Scripts/pip.exe install -r requirements.txt

run: venv/Scripts/activate.bat
	./venv/Scripts/python.exe ./src/main.py
