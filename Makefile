PROJECTS := $(shell find . -mindepth 2 -name Makefile | xargs dirname)
TARGET = all

all: $(PROJECTS)

clean: TARGET = clean
clean: $(PROJECTS)

new:
	@./bin/create-project

$(PROJECTS):
	@$(MAKE) -C $@ $(TARGET)

.PHONY: $(PROJECTS)
