.PHONY: makemigrate
makemigrate:
	docker-compose run --rm web alembic revision --autogenerate

.PHONY: lint-format
lint-format:
	docker-compose run --rm web black .
	docker-compose run --rm web isort .
	docker-compose run --rm web flake8 .

.PHONY: migrate
migrate:
	docker-compose run --rm web alembic upgrade head

.PHONY: import-data
import-data:
	docker-compose run --rm web python /app/server/commands/import.py all
