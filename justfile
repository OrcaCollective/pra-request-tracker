IS_PROD := env_var_or_default("IS_PROD", "")
COMPOSE_FILE := if IS_PROD == "true" {"-f docker-compose-prod.yml "} else {""}
DC := "docker-compose " + COMPOSE_FILE
RUN := DC + " run --rm "
DJANGO := "django"
MANAGE := RUN + DJANGO + " python manage.py"
set dotenv-load := false


env:
	if [ ! -f ".env" ]; then cp .env.example .env; fi

shell: env
	{{ MANAGE }} shell

logs service="": env
	{{ DC }} logs -f {{ service }}

build:
	{{ DC }} build

up service="":
	{{ DC }} up -d {{ service }}

down:
	{{ DC }} down

restart: down up

rebuild: down build up

freshstart: env
	# Tear down existing containers, remove volume
	{{ DC }} down -v
	just build
	just up

createsuperuser: env
	{{ MANAGE }} createsuperuser

makemigrations: env
	{{ MANAGE }} makemigrations

migrate: env
	{{ MANAGE }} migrate

test: env
	{{ RUN }} {{ DJANGO }} coverage run -m pytest

coverage: test
	{{ RUN }} {{ DJANGO }} coverage html
	open htmlcov/index.html

run service +args:
	{{ RUN }} {{ service }} {{ args }}

install: env
	pip install -r requirements-dev.txt
	pre-commit install

lint: env
	pre-commit run --all-files
