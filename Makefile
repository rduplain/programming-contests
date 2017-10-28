PROJECTS := $(shell find * -maxdepth 0 -type d)

all: $(PROJECTS)

$(PROJECTS):
	@$(MAKE) -C $@

.PHONY: $(PROJECTS)
