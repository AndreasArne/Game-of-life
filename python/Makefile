#!/usr/bin/env make -f
#
# Makefile for Python version of Game of life
#
.DEFAULT_GOAL := test

# Decide if use python3 or python
ifeq (python3 --version > /dev/null, 1)
	py = python3
else
	py = python
endif



.PHONY: exec-tests
exec-tests:
	@echo "Run tests in runner.py"
	@cd tests && ${py} -m coverage run --rcfile=../.coveragerc runner.py



.PHONY: test
test: exec-tests
	@cd tests && ${py} -m coverage report --rcfile=../.coveragerc



.PHONY: test-html
test-html: exec-tests
	@cd tests && ${py} -m coverage html --rcfile=../.coveragerc && firefox coverage_html/index.html &



.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm tests/.coverage
	rm -rf tests/coverage_html
