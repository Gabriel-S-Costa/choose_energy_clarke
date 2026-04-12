dev-up:
	fastapi dev app/main.py

check:
	ruff check && ruff format --check

lint:
	ruff check --fix && ruff format

test:
	pytest tests -vv -p no:warnings