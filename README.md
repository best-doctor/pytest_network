# pytest-network

[![Build Status](https://travis-ci.org/best-doctor/pytest_network.svg?branch=master)](https://travis-ci.org/best-doctor/pytest_network)
[![Maintainability](https://api.codeclimate.com/v1/badges/1f243263e78f38f92a31/maintainability)](https://codeclimate.com/github/best-doctor/pytest_network/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1f243263e78f38f92a31/test_coverage)](https://codeclimate.com/github/best-doctor/pytest_network/test_coverage)
[![PyPI version](https://badge.fury.io/py/pytest_network.svg)](https://badge.fury.io/py/pytest_network)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest_network)](https://pypi.org/project/pytest_network/)

A simple pytest plugin to disable network on socket level.

## Installation

`$ pip install pytest-network`

## Usage

`pytest-network` has a flag `--disable-network` that will raise an error
if tests will try to use `socket.socket.connect`

You can use it directly like:

`$ python3 -m pytest --disable-network`

or add this flag as the default behavior in your `pytest.ini`:

```ini
[pytest]
addopts = --disable-network
```

Also you can directly disable network:

```python3
import requests


def test_network_request_raises_error(disable_network):
    response = requests.get('https://github.com')  # this will raise an exception

    assert response.status_code == 200
```

or directly enable (if you have default `--disable-network` flag):

```python3
import requests


def test_network_request_is_ok(enable_network):
    response = requests.get('https://github.com')

    assert response.status_code == 200  # this will pass
```

You can use test marks instead of fixtures: add `@pytest.mark.disable_network`
or `@pytest.mark.enable_network` to disable or enable network in test.

## Development

To setup development environment you must first create a virtual environment.
For example:

`$ python3.8 -m venv <venv-name>`

After that install all requirements:

`$ pip install -r requirements.txt`

And install plugin itself (inside project directory and virtual environment):

`$ pip install -e .`

Check that tests are running:

`$ make test`

## Contributing

We would love you to contribute to our project. It's simple:

* Create an issue with bug you found or proposal you have.
  Wait for approve from maintainer.
* Create a pull request. Make sure all checks are green.
* Fix review comments if any.
* Be awesome.

Here are useful tips:

* You can run all checks and tests with make check.
  Please do it before TravisCI does.
* We use [BestDoctor python styleguide](https://github.com/best-doctor/guides/blob/master/guides/en/python_styleguide.md).
* We respect [Django CoC](https://www.djangoproject.com/conduct/).
  Make soft, not bullshit.
