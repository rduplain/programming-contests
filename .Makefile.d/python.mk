SHELL := /bin/bash

test-%:
	@time python main.py < sample/$*.in | tee $*.out
	@echo "---"
	@diff sample/$*.ans $*.out

clean:
	rm -f *.out

version:
	@python --version
	@echo "---"
