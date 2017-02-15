tests: unit behave

unit:
	python -m unittest discover src/tests/unit_tests

behave:
	behave src/tests/acceptance_tests
