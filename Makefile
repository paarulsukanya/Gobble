REQUIREMENTS_FILE=requirements.txt

setup:
	pip install -r $(REQUIREMENTS_FILE)

run:
	python gobble.py

test:
	python tests/gobble_tests.py


