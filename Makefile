# use some sensible default shell settings
SHELL := /bin/bash -o pipefail
.SILENT:
.DEFAULT_GOAL := start

APP_NAME ?= lab-app
CONTAINERS := $(shell docker ps -aq -f name=${APP_NAME})

# DOCKER TASKS
# Build the container
build: ## Build the container
	echo -e '\nBuilding docker container...'
	docker build -t $(APP_NAME) .

run:
	echo -e '\nRunning docker container...'
	docker run -d -p=80:5000 --name="$(APP_NAME)" $(APP_NAME) 2>&1 >/dev/null
	echo -e 'Run successful.\n\nNavigate to http://localhost'

start: destroy build run

destroy: ## Stop and remove a running container
	if [ $(CONTAINERS) ] ; then \
		docker rm -f $(APP_NAME) 2>&1 >/dev/null; \
		echo -e 'Container slate cleaned.'; \
	fi