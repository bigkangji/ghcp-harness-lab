.PHONY: lint test verify

lint:
	python3 -m ruff check .

test:
	python3 -m unittest discover -s tests -v

verify: lint test