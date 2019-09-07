__author__ = 'anna'
import pytest

@pytest.fixture()
def method_set_up():
    print('Method setup')
    yield
    print('Method teardown')

@pytest.fixture(scope='module')
def module_set_up(browser, os_type, server_time):
    print('Module setup')
    if browser == 'Firefox':
        print('Running test on FF')
    else:
        print('Running test on Chrome')

    if os_type == 'Linux':
        print('Running test on Linux')
    else:
        print('Running test on OS X')

    if server_time == "EST":
        print('EST')
    else:
        print("PDT")
    yield
    print('Module teardown')

@pytest.fixture(scope='class')
def module_set_up_level_to_test_a_class(request, browser, os_type):
    print('Module setup')
    if browser == 'Firefox':
        value = 10
        print('Running test on FF')
    else:
        value = 20
        print('Running test on Chrome')

    if os_type == 'Linux':
        print('Running test on Linux')
    else:
        print('Running test on OS X')

    # to pass value to the TestClassDemo2 if class requests it!! while initializing instance
    if request.cls:  #.cls - means class context (level)
        request.cls.value = value
    yield value
    print('Module teardown')

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--serverTime", help="Type the server time")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def os_type(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope='session')
def server_time(request):
    return request.config.getoption("--serverTime")
