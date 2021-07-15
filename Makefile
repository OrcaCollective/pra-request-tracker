ifeq ($(OS),Windows_NT)
    detected_OS := Windows
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
endif

ifeq ($(detected_OS), Linux)
	DOCKER_COMPOSE ?= docker-compose
else
	DOCKER_COMPOSE ?= docker compose
endif

FILE ?= local.yml
DC = $(DOCKER_COMPOSE) --file=$(FILE)
RUN = $(DC) run --rm
DJANGO = django
MANAGE = $(RUN) $(DJANGO) python pra_request_tracker/manage.py


.env:
	cp .env.example .env


.PHONY: shell
shell: .env
	$(MANAGE) shell


.PHONY: logs
logs: .env
	$(DC) logs -f $(DJANGO)


.PHONY: down
down: .env
	$(DC) down


.PHONY: up
up: .env
	$(DC) up -d


.PHONY: restart
restart: down up


.PHONY: build
build: .env
	$(DC) build


.PHONY: createsuperuser
createsuperuser: .env
	$(MANAGE) createsuperuser


.PHONY: rebuild
rebuild: down build up


.PHONY: freshstart
freshstart: .env
	$(DC) down -v
	$(MAKE) build
	$(MAKE) up


.PHONY: makemigrations
makemigrations: .env
	$(MANAGE) makemigrations


.PHONY: migration
migrate: .env
	$(MANAGE) migrate


.PHONY: types
types: .env
	$(RUN) $(DJANGO) mypy pra_request_tracker


.PHONY: test
test: .env
	$(RUN) $(DJANGO) coverage run -m pytest


.PHONY: coverage
coverage: test
	$(RUN) $(DJANGO) coverage html
	open htmlcov/index.html


.PHONY: install
install: .env
	pip install -r requirements/local.txt
	pre-commit install


.PHONY: lint
lint:
	pre-commit run --all-files
