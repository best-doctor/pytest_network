test:
	python3 -m pytest

style:
	flake8 pytest_network.py
	mdl README.md

requirements:
	safety check -r requirements.txt

check:
	make test style requirements

