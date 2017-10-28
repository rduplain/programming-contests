test-%:
	@time python main.py < sample/$*.in | tee $*.out
	@echo "---"
	@diff sample/$*.ans $*.out

version:
	@python --version
	@echo "---"
