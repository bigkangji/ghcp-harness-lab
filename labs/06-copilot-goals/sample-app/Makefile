.PHONY: lint test verify

lint:
	python3 -m py_compile goalkeeper.py

test:
	python3 -m unittest discover -s tests -v

verify: lint test
