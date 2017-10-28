PROJECTS := $(shell find * -maxdepth 0 -type d)
TARGET = all

all: $(PROJECTS)

clean: TARGET = clean
clean: $(PROJECTS)

$(PROJECTS):
	@$(MAKE) -C $@ $(TARGET)

.PHONY: $(PROJECTS)
