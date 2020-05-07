test:
	python -m pytest --cov=pytest_network --cov-report=xml

style:
	flake8 pytest_network.py
	mdl README.md

types:
	mypy .

requirements:
	safety check -r requirements.txt

check:
	make test style types requirements

