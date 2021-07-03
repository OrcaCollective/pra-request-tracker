DOCKER_COMPOSE ?= docker compose
FILE ?= local.yml
DC = $(DOCKER_COMPOSE) --file=$(FILE)
RUN = $(DC) run --rm
DJANGO = django
MANAGE = $(RUN) $(DJANGO) python manage.py

.PHONY: shell
shell:
	$(MANAGE) shell


.PHONY: logs
logs:
	$(DC) logs -f $(DJANGO)


.PHONY: down
down:
	$(DC) down


.PHONY: up
up:
	$(DC) up -d


.PHONY: restart
restart: down up


.PHONY: build
build:
	$(DC) build


.PHONY: createsuperuser
createsuperuser:
	$(MANAGE) createsuperuser


.PHONY: rebuild
rebuild: down build up


.PHONY: freshstart
freshstart:
	$(DC) down -v
	$(MAKE) build
	$(MAKE) up


.PHONY: makemigrations
makemigrations:
	$(MANAGE) makemigrations


.PHONY: migration
migrate:
	$(MANAGE) migrate


.PHONY: types
types:
	$(RUN) $(DJANGO) mypy pra_request_tracker


.PHONY: test
test:
	$(RUN) $(DJANGO) coverage run -m pytest


.PHONY: coverage
coverage: test
	$(RUN) $(DJANGO) coverage html
	open htmlcov/index.html


.PHONY: install
install:
	pip install -r requirements/local.txt
	pre-commit install


.PHONY: lint
lint:
	pre-commit run --all-files
