import socket

import pytest


class NetworkUsageException(Exception):
    pass


_original_connect = socket.socket.connect


def pytest_addoption(parser):
    group = parser.getgroup('network')
    group.addoption(
        '--disable-network',
        action='store_true',
        dest='disable_network',
        help='Monkeypatch socket.socket.connect.'
    )


@pytest.fixture(autouse=True)
def _network_marker(request):
    if request.config.getoption('--disable-network'):
        request.getfixturevalue('disable_network')


def patched_connect(*args, **kwargs):
    raise NetworkUsageException


@pytest.fixture
def enable_network():
    socket.socket.connect = _original_connect
    yield
    socket.socket.connect = patched_connect


@pytest.fixture
def disable_network():
    socket.socket.connect = patched_connect
    yield
    socket.socket.connect = _original_connect
