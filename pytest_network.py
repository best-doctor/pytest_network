import socket

import pytest


class NetworkUsageException(Exception):  # pragma: no cover
    pass


_original_connect = socket.socket.connect  # pragma: no cover


def pytest_addoption(parser):
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


@pytest.fixture(autouse=True)  # pragma: no cover
def _network_marker(request):
    if request.config.getoption('--disable-network'):
        request.getfixturevalue('disable_network')


def patched_connect(*args, **kwargs):  # pragma: no cover
    raise NetworkUsageException


@pytest.fixture  # pragma: no cover
def enable_network():
    socket.socket.connect = _original_connect
    yield
    socket.socket.connect = patched_connect


@pytest.fixture  # pragma: no cover
def disable_network():
    socket.socket.connect = patched_connect
    yield
    socket.socket.connect = _original_connect


def pytest_runtest_call(item):
    marks_to_connect_mapper = [
        ('disable_network', patched_connect),
        ('enable_network', _original_connect),
    ]
    for mark_name, connect_mock in marks_to_connect_mapper:
        if list(item.iter_markers(name=mark_name)):
            if socket.socket.connect != connect_mock:
                socket.socket.connect = connect_mock


def pytest_runtest_teardown(item):
    marks_to_connect_mapper = [
        ('disable_network', _original_connect),
        ('enable_network', patched_connect),
    ]
    for mark_name, connect_mock in marks_to_connect_mapper:
        if list(item.iter_markers(name=mark_name)):
            if socket.socket.connect != connect_mock:
                socket.socket.connect = connect_mock
