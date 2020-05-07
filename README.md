# pytest-network

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


def test_network_request_is_ok(disable_network):
    response = requests.get('https://github.com')

    assert response.status_code == 200  # this will pass
```

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
* We use [BestDoctor python styleguide](https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md).
  Sorry, styleguide is available only in Russian for now.
* We respect [Django CoC](https://www.djangoproject.com/conduct/).
  Make soft, not bullshit.
