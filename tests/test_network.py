import pytest
from pytest_network import patched_connect, NetworkUsageException


def test_disable_network_fixture_raiese_exception(testdir):
    testdir.makepyfile(
        """
        import urllib.request

        import pytest


        def test_hello_default(disable_network):
            with pytest.raises(Exception):
                urllib.request.urlopen('http://httpbin.org/robots.txt')
        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}


@pytest.mark.usefixtures('disable_network_addopt')
def test_disable_network_addopt_raises_exception(testdir):
    testdir.makepyfile(
        """
        import urllib.request

        import pytest


        def test_hello_default():
            with pytest.raises(Exception):
                urllib.request.urlopen('http://httpbin.org/robots.txt')
        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}


@pytest.mark.usefixtures('disable_network_addopt')
def test_enable_network_fixture_enables_connect(testdir):
    testdir.makepyfile(
        """
        import urllib.request

        import pytest


        def test_hello_default(enable_network):
            response = urllib.request.urlopen('http://httpbin.org/robots.txt')

            assert response.status == 200
        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}


def test_disable_pytest_mark_workds(testdir):
    testdir.makepyfile(
        """
        import urllib.request

        import pytest


        @pytest.mark.disable_network
        def test_hello_default():
            with pytest.raises(Exception):
                urllib.request.urlopen('http://httpbin.org/robots.txt')

        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}


@pytest.mark.usefixtures('disable_network_addopt')
def test_enable_pytest_mark_workds(testdir):
    testdir.makepyfile(
        """
        import urllib.request

        import pytest


        @pytest.mark.enable_network
        def test_hello_default():
            response = urllib.request.urlopen('http://httpbin.org/robots.txt')

            assert response.status == 200
        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}


def test_patched_connect_always_raises_error():
    with pytest.raises(NetworkUsageException):
        patched_connect()
