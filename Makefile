.PHONY: default install test

default: test

install:
	pipenv install --dev --skipback

test:
	PYTHONPATH=./src pytest

