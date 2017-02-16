tests: unit behave

unit:
	python -m unittest discover monopoly/tests/unit_tests

behave:
	behave monopoly/tests/acceptance_tests
