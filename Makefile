SHELL := /bin/bash

PROJECTS := $(shell find . -mindepth 2 -name Makefile | xargs -L 1 dirname)
TARGET = all

all: $(PROJECTS)

clean: TARGET = clean
clean: $(PROJECTS)

new:
	@./bin/create-project

new-without-samples:
	@./bin/create-project --no-samples

$(PROJECTS):
	@$(MAKE) -C $@ $(TARGET)

.PHONY: $(PROJECTS)
