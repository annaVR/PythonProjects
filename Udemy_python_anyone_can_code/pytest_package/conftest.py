__author__ = 'anna'
import pytest

@pytest.fixture()
def method_set_up():
    print('Method setup')
    yield
    print('Method teardown')

@pytest.fixture(scope='module')
def module_set_up(browser, os_type):
    print('Module setup')
    if browser == 'Firefox':
        print('Running test on FF')
    else:
        print('Running test on Chrome')

    if os_type == 'Linux':
        print('Running test on Linux')
    else:
        print('Running test on OS X')
    yield
    print('Module teardown')

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def os_type(request):
    return request.config.getoption("--osType")