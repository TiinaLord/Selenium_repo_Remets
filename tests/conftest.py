import os
import random
import pytest
import logging
import datetime
import json
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.111:8081")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", default="192.168.0.111")
    parser.addoption("--platform", default="Linux")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    platform = request.config.getoption("--platform")
    executor_url = f"http://{executor}:4444/wd/hub"
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    logs = request.config.getoption("--logs")
    vnc = request.config.getoption("--vnc")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = EdgeOptions()
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError

    if browser != "safari":
        service.set_capability("platformName", platform)

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON)

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=service
    )

    caps = {
        "browserName": browser,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": os.getenv("BUILD_NUMBER", str(random.randint(9000, 10000))),
            "enableLog": logs,

        },
        "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        service.set_capability(k, v)

    driver.maximize_window()
    driver.get(url)
    driver.url = url
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info("Browser %s started" % browser)

    def fin():
        attach = driver.get_screenshot_as_png()
        if request.node.rep_setup.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
