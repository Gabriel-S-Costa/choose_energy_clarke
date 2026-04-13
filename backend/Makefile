dev-up:
	fastapi dev app/main.py

up:
	uvicorn app.main:app --reload

check:
	ruff check && ruff format --check

lint:
	ruff check --fix && ruff format

test:
	pytest tests -vv -p no:warnings