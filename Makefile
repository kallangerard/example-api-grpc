YARN_VERSION = 3.3.1
COMPOSE_RUN_NODE = docker-compose run --rm node
COMPOSE_UP_NODE = docker-compose up -d node
COMPOSE_UP_NODE_DEV = docker-compose up node_dev
COMPOSE_RUN_DEV = docker-compose run --rm dev --build
COMPOSE_UP_PYTHON = docker-compose up -d python
PYTHON_RUN = poetry run

all:
	$(MAKE) ciTest

ciTest: pruneDocker deps build serve test prune

ciDeploy: pruneDocker deps build serve test deploy prune

deps: _depsNode _depsPython

_depsNode:
	corepack prepare yarn@$(YARN_VERSION) --activate
	yarn node-packages/* install

_depsPython:
	poetry install

devFrontend: deps
	make _devFrontend
_devFrontend:
	yarn node-packages/frontend dev

devApi: deps
	make _devApi
_devApi:
	$(PYTHON_RUN) uvicorn escrow-service.main:app --reload

testApi: depsApi
	make _testApi
_testApi:
	$(PYTHON_RUN) pytest

pruneDocker:
	docker-compose down --remove-orphans

