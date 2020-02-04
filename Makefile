# use some sensible default shell settings
SHELL := /bin/bash -o pipefail
.SILENT:
.DEFAULT_GOAL := help

# default variables
export VERSION ?= 1.0
export LAST_COMMIT_SHA ?= $(shell git rev-parse --short HEAD)

DOCKER_CONTAINER_LIST := $(shell docker ps -a -q)

##@ Entry Points
.PHONY: build
build: ## Build and test docker image artifact
	docker build -t lab:latest .
	docker run -d -p 5000:5000 lab

.PHONY: destroy
destroy: ## Destroy containers made
	if [ -n "$(DOCKER_CONTAINER_LIST)" ]; \
	then \
		docker stop "$(DOCKER_CONTAINER_LIST)"; \
		docker rm "$(DOCKER_CONTAINER_LIST)"; \
	fi