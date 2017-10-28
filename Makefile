PROJECTS := $(shell find . -mindepth 2 -name Makefile | xargs dirname)
TARGET = all

all: $(PROJECTS)

clean: TARGET = clean
clean: $(PROJECTS)

$(PROJECTS):
	@$(MAKE) -C $@ $(TARGET)

.PHONY: $(PROJECTS)
