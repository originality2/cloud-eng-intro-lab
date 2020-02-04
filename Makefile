# use some sensible default shell settings
SHELL := /bin/bash -o pipefail
.SILENT:
.DEFAULT_GOAL := start

APP_NAME ?= lab-app

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -t $(APP_NAME) .

run:
	docker run -d -p=80:5000 --name="$(APP_NAME)" $(APP_NAME)

start: destroy build run

destroy: ## Stop and remove a running container
	docker rm -qf $(APP_NAME) || true