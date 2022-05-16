from selenium import webdriver
from configfiles.webdriverfactory import Webdriverfactory
import unittest
import pytest


@pytest.fixture(scope="class")
def oneTimeSetUp6(browser, request):
    drv=Webdriverfactory(browser)
    global driver
    driver = drv.driver_instance()
    #driver.get("https://pcpress.rs/prodavnica/index.php")
    driver.maximize_window()
    driver.implicitly_wait(10)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()

@pytest.fixture()
def setUp6():
    driver.get("https://pcpress.rs/prodavnica/index.php")
    print("Setup before every method")
    yield
    print("Setup after every method")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")







