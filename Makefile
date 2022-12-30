COMPOSE_RUN_NODE = docker-compose run --rm node
COMPOSE_UP_NODE = docker-compose up -d node
COMPOSE_UP_NODE_DEV = docker-compose up node_dev
COMPOSE_RUN_PYTHON = docker-compose run --rm python
COMPOSE_UP_PYTHON = docker-compose up -d python

all:
	ENVFILE=env.example $(MAKE) ciTest

ciTest: pruneDocker deps build serve test prune

ciDeploy: pruneDocker deps build serve test deploy prune

envfile:
	cp -f $(ENVFILE) .env

depsFrontend:
	$(COMPOSE_RUN_NODE) install

depsApi:
	docker-compose build python

upgradeDepsFrontend:
	$(COMPOSE_RUN_NODE) upgrade

shell:
	$(COMPOSE_RUN_NODE) bash

dev:
	COMPOSE_COMMAND="make _dev" $(COMPOSE_UP_NODE_DEV)
_dev:
	yarn run dev

build:
	$(COMPOSE_RUN_NODE) make _build
_build:
	yarn run build

devApi:
	$(COMPOSE_RUN_PYTHON) make _devApi
_devApi:
	uvicorn escrow-service.main:app --reload

testApi:
	$(COMPOSE_RUN_PYTHON) make _testApi
_testApi:
	pytest

pruneDocker:
	docker-compose down --remove-orphans

