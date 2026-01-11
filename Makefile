run:
	fastapi dev ./src/main.py
freeze:
	pip freeze > requirements.txt