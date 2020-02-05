test:
		python3 -m pytest

style:
		flake8 pytest_network.py

check:
		make test style
