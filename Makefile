# Simple Makefile for Lead-Gen-Pro

setup:
	poetry install

run:
	poetry run uvicorn lead_gen_pro.app:app --reload --port 8000

docker-build:
	docker build -t lead-gen-pro .

docker-run:
	docker run -p 8000:8000 lead-gen-pro

test:
	poetry run pytest -v

format:
	poetry run black .
	poetry run ruff --fix .