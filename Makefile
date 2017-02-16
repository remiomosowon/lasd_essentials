.PHONY: test unit behave acceptance tests

help:
	@echo "test - run unit tests with unittest"
	@echo "behave - run acceptance tests with behave"
	@echo "tests - run both unit and acceptance tests"

test: unit
unit:
	python -m unittest discover -v monopoly/tests/unit_tests

behave: acceptance
acceptance:
	behave monopoly/tests/acceptance_tests

tests: unit acceptance
