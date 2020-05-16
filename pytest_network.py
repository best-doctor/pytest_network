import socket

import pytest


class NetworkUsageException(Exception):  # pragma: no cover
    pass


_original_connect = socket.socket.connect  # pragma: no cover


def pytest_addoption(parser):  # pragma: no cover
    group = parser.getgroup('network')
    group.addoption(
        '--disable-network',
        action='store_true',
        dest='disable_network',
        help='Monkeypatch socket.socket.connect.',
    )


def pytest_configure(config):  # pragma: no cover
    config.addinivalue_line('markers', 'disable_network: disables network in marked test')
    config.addinivalue_line('markers', 'enable_network: disables network in marked test')


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


def pytest_runtest_call(item):
    if list(item.iter_markers(name='disable_network')):
        socket.socket.connect = patched_connect
    if list(item.iter_markers(name='enable_network')):
        socket.socket.connect = _original_connect


def pytest_runtest_teardown(item):
    if list(item.iter_markers(name='disable_network')):
        socket.socket.connect = _original_connect
    elif list(item.iter_markers(name='enable_network')):
        socket.socket.connect = patched_connect
