all: version test-01 test-02 test-03 test-user-01

test-user-%:
	@time python main.py < sample/user-$*.in > user-$*.out
	@echo "---"
	@diff -q sample/user-$*.ans user-$*.out

include ../.Makefile.d/python.mk
