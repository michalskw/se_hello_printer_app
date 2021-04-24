.PHONY: test

deps:
	pip install -r requirements.txt;
	pip install -r requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s

lint:
	flake8 hello_world test

run:
	python main.py
