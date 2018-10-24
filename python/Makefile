#!/usr/bin/env make -f
#
# Makefile for Python version of Game of life
#

# ---------------------------------------------------------------------------
#
# General setup
#

# Set default target
.DEFAULT_GOAL := test

# Decide if use python3 or python
 py = python3
 ifeq (, $(@shell which python3))
 	py = python
 endif

# Detect OS
OS = $(shell uname -s)

# Defaults
ECHO = echo

# Make adjustments based on OS
ifneq (, $(findstring CYGWIN, $(OS)))
	ECHO = /bin/echo -e
endif

# Colors and helptext
NO_COLOR	= \033[0m
ACTION		= \033[32;01m
OK_COLOR	= \033[32;01m
ERROR_COLOR	= \033[31;01m
WARN_COLOR	= \033[33;01m

# Which makefile am I in?
WHERE-AM-I = $(CURDIR)/$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
THIS_MAKEFILE := $(call WHERE-AM-I)

# Echo some nice helptext based on the target comment
HELPTEXT = $(ECHO) "$(ACTION)--->" `egrep "^\# target: $(1) " $(THIS_MAKEFILE) | sed "s/\# target: $(1)[ ]*-[ ]* / /g"` "$(NO_COLOR)"



# ----------------------------------------------------------------------------
#
# Highlevel targets
#
# target: help                    - Displays help with targets available.
.PHONY:  help
help:
	@$(call HELPTEXT,$@)
	@echo "Usage:"
	@echo " make [target] ..."
	@echo "target:"
	@egrep "^# target:" Makefile | sed 's/# target: / /g'



# target: exec-tests              - Run tests in tests/runner.py with coverage.py
.PHONY: exec-tests
exec-tests:
	@$(ECHO) "$(ACTION)---> Running all tests in tests/" "$(NO_COLOR)"
	@cd tests && ${py} -m coverage run --rcfile=../.coveragerc runner.py \
		&& $(ECHO) "$(OK_COLOR)All tests passed " "$(NO_COLOR)" \
		|| $(ECHO) "$(ERROR_COLOR)Tests faild" "$(NO_COLOR)"



# target: test                    - Run tests and display code coverage
.PHONY: test
test: exec-tests
	@cd tests && ${py} -m coverage report --rcfile=../.coveragerc



# target: test-html               - Run tests and display detailed code coverage with html
.PHONY: test-html
test-html: exec-tests
	@cd tests && ${py} -m coverage html --rcfile=../.coveragerc && firefox coverage_html/index.html &



# target: clean                   - Remove all generated files
.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm tests/.coverage
	rm -rf tests/coverage_html
