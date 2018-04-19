REQUIREMENTS_FILE=requirements.txt

setup:
	pip install --upgrade pip
	pip install -r $(REQUIREMENTS_FILE)

run:
	java -jar dynamoDB/DynamoDBLocal.jar -dbPath ./common/ &
	python gobble.py &

test:
	python tests/gobble_tests.py


