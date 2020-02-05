import pytest

pytest_plugins = ['pytester']


@pytest.fixture
def disable_network_addopt(testdir):
    return testdir.makeini(
        """
        [pytest]
        addopts = --disable-network
        """
    )
