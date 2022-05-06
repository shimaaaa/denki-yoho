.PHONY: migrate
migrate:
	cd /app/server && alembic upgrade head

.PHONY: makemigrate
makemigrate:
	cd /app/server && alembic revision --autogenerate

.PHONY: lint-format
lint-format:
	black .
	isort .
	flake8 .

.PHONY: container-migrate
container-migrate:
	docker-compose run --rm web alembic upgrade head
