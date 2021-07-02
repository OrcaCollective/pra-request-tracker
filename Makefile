DOCKER_COMPOSE ?= docker compose
FILE ?= local.yml
DC = $(DOCKER_COMPOSE) --file=$(FILE)
RUN = $(DC) run --rm
DJANGO = django
MANAGE = $(RUN) $(DJANGO) python manage.py

shell:
	$(MANAGE) shell


logs:
	$(DC) logs -f $(DJANGO)


down:
	$(DC) down


up:
	$(DC) up -d


restart: down up


build:
	$(DC) build


createsuperuser:
	$(MANAGE) createsuperuser


freshstart: down build up


makemigrations:
	$(MANAGE) makemigrations


migrate:
	$(MANAGE) migrate


types:
	$(RUN) $(DJANGO) mypy pra_request_tracker


test:
	$(RUN) $(DJANGO) coverage run -m pytest


coverage: test
	$(RUN) $(DJANGO) coverage html
	open htmlcov/index.html


install:
	pip install -r requirements/local.txt
	pre-commit install


lint:
	pre-commit run --all-files
