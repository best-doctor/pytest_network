test:
	python -m pytest --cov=pytest_network --cov-report=xml

style:
	flake8 pytest_network.py
	mdl README.md

requirements:
	safety check -r requirements.txt

check:
	make test style requirements

