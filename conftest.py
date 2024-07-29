import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="yandex", choices=["yandex", "firefox", "chrome"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.0.107:8081")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "yandex":
        yandex_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'drivers', 'yandexdriver.exe'))
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(executable_path=yandex_driver_path)
        driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size("1920", "1080")
    yield driver
    driver.quit()
