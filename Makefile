ifndef VENVNAME
  VENVNAME = venv
endif

ifeq ($(OS),Windows_NT)
	CURRENT_DIR = $(shell cd)
	INTERPRETER_DIR = $(CURRENT_DIR)/$(VENVNAME)/Scripts
else
	CURRENT_DIR = $(shell pwd)
	INTERPRETER_DIR = $(CURRENT_DIR)/$(VENVNAME)/bin
endif

PYTHON=$(INTERPRETER_DIR)/python

deps:
	$(INTERPRETER_DIR)/pip install -r ./requirements.txt


migrate:
	-flask db init
	-flask db migrate
	flask db upgrade

build:
	docker build -t ml_test .

run:
	docker run -d -p 1088:80 ml_test
