import pytest
import logging
import datetime
import allure
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions, SafariOptions
import os
import random

EXECUTOR = 'localhost'
URL = 'http://192.168.1.7'  # 'http://192.168.1.7', 'https://demo.opencart.com', http://192.168.1.2:8888


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", action="store", default=EXECUTOR)
    parser.addoption("--url", action="store", default=URL)
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--bv")
    parser.addoption("--vnc", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")

    CMD_EXECUTOR = f'http://{executor}:4444/wd/hub'

    logger = logging.getLogger(request.node.name)
    logger.setLevel(level=log_level)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
    elif browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
    elif browser_name == "safari":
        options = SafariOptions()
    else:
        raise ValueError(f'Driver {browser_name} not supported.')

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": os.getenv("BUILD_NUMBER", str(random.randint(9000, 10000))),
            "screenResolution": "1280x1440",
            "timeZone": "Europe/Moscow",
            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
        },
        "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    driver = webdriver.Remote(
        command_executor=CMD_EXECUTOR,
        options=options)

    if maximize:
        driver.maximize_window()

    driver.url = url
    driver.logger = logger
    logger.info("Browser %s started" % browser_name)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    with allure.step("Browser %s started" % browser_name):
        return driver
