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
ifeq (, $(@shell which python3))
	py = python3
else
	py = python
endif
# Decide if use pip3 or pip
ifeq (, $(@shell which pip3))
	pip = pip3
else
	pip = pip
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



# target: run <pattern=pattern>   - Start game, game/logic.py. Optional argument with pattern
.PHONY: run
run:
	@${py} -m game.logic ${pattern}



# target: validate                - Validate code with pylint
.PHONY: validate
validate:
	@pylint game tests \
		&& $(ECHO) "$(OK_COLOR)Code is valid " "$(NO_COLOR)" \
		|| $(ECHO) "$(ERROR_COLOR)Clean up your code!" "$(NO_COLOR)"



# target: exec-tests              - Run tests in tests/runner.py with coverage.py
.PHONY: exec-tests
exec-tests: clean
	@$(ECHO) "$(ACTION)---> Running all tests in tests/" "$(NO_COLOR)"
	@${py} -m coverage run tests/runner.py \
		&& $(ECHO) "$(OK_COLOR)All tests passed " "$(NO_COLOR)" \
		|| $(ECHO) "$(ERROR_COLOR)Tests faild" "$(NO_COLOR)"



# target: test                    - Run tests and display code coverage
.PHONY: test
test: exec-tests
	echo "${py}"

	${py} -m coverage report



# target: test-html               - Run tests and display detailed code coverage with html
.PHONY: test-html
test-html: exec-tests
	${py} -m coverage html && firefox tests/coverage_html/index.html &



# target: clean                   - Remove all generated files
.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf game/__pycache__
	rm -rf tests/__pycache__
	rm -f .coverage
	rm -rf tests/coverage_html



# target: install                 - Install all Python packages specified in requirement.txt
.PHONY: install
install:
	${pip} install -r requirements.txt
