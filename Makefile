.PHONY: makemigrate
makemigrate:
	docker-compose run --rm api alembic revision --autogenerate

.PHONY: lint-format
lint-format:
	docker-compose run --rm api black .
	docker-compose run --rm api isort .
	docker-compose run --rm api flake8 .

.PHONY: migrate
migrate:
	docker-compose run --rm api alembic upgrade head

.PHONY: import-data
import-data:
	docker-compose run --rm api python /app/server/commands/import.py all

.PHONY: generate-api-client
generate-api-client:
	docker-compose run --rm ui curl -o /app/ui/openapi.json http://api:8000/openapi.json
	docker-compose run --rm ui npm run generate-client
