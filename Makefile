# use some sensible default shell settings
SHELL := /bin/bash -o pipefail
.SILENT:
.DEFAULT_GOAL := help

# default variables
export VERSION ?= 1.0
export LAST_COMMIT_SHA ?= $(shell git rev-parse --short HEAD)

# import config.
# You can change the default config with `make cnf="config_special.env" build`
cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

# import deploy config
# You can change the default deploy config with `make cnf="deploy_special.env" release`
dpl ?= deploy.env
include $(dpl)
export $(shell sed 's/=.*//' $(dpl))

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -t $(APP_NAME) .

run: ## Run container on port configured in `config.env`
	docker run -d -p=$(PORT):$(PORT) --name="$(APP_NAME)" $(APP_NAME)

start: build run

destroy: ## Stop and remove a running container
	docker stop $(APP_NAME); docker rm $(APP_NAME)