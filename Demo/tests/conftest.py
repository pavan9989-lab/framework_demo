import pytest
from selenium import webdriver


@pytest.yield_fixture()
def setUp():
    print("running method level setup")
    yield
    print("running method level tearDown")



@pytest.yield_fixture(scope="class")
def oneTimeSetUp(browser):
    print("running one time set up")
    if browser == 'firefox':
        print("running tests on ff")
    else:
        print("running tests on chrome")

    yield
    print("running one time tear down")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Tepe of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")