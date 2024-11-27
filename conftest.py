import logging
import os
import time

import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.AdminLoginPage import AdminLoginPage


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logging.getLogger().addHandler(console_handler)

    logging.info('Logging setup complete')

configure_logging()
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'



def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["yandex", "firefox", "chrome"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--browser-version", default="128.0", help="Browser version")
    parser.addoption("--url", default="http://localhost:8080")
    parser.addoption("--remote", action="store_true", help="Run tests on Selenoid")
    parser.addoption("--vnc", action="store_true", help="Enable VNC for Selenoid")
    parser.addoption("--mobile", action="store_true", help="Enable mobile view")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--threads", default="1", help="Number of threads")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser-version")  # Получаем версию браузера
    headless = request.config.getoption("--headless")
    remote = request.config.getoption("--remote")
    mobile = request.config.getoption("--mobile")
    vnc = request.config.getoption("--vnc")
    executor = request.config.getoption("--executor")
    threads = request.config.getoption("--threads")

    driver = None
    logging.info(f"Starting browser: {browser_name}, version: {browser_version}, headless: {headless}, remote: {remote}, mobile: {mobile}, vnc: {vnc}, threads: {threads}")
    if remote:
        selenoid_url = f"http://{executor}:4444/wd/hub"
        options = None

        if browser_name == "chrome":
            options = ChromeOptions()
            options.set_capability("browserVersion", browser_version)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.set_capability("browserVersion", browser_version)


        options.set_capability("browserName", browser_name)
        if vnc:
            options.set_capability("selenoid:options", {"enableVNC": True})

        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
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
    if not mobile:
        driver.maximize_window()
    yield driver
    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML
        )
    driver.quit()


@pytest.fixture(scope="function")
def administrator_login_token(browser, url):
    browser.get(f"{url}/administration/")
    admin_page = AdminLoginPage(browser)
    admin_page.set_login("user")
    admin_page.set_password("bitnami")
    admin_page.login()
    time.sleep(1)
    current_url = browser.current_url
    token = current_url.split('token=')[1]
    yield token


@pytest.fixture
def delete_product(browser, url):
    product_ids = []
    token, cookies = AdminLoginPage(browser).get_admin_token_and_cookies(url)

    def _delete_product(created_product_id):
        product_ids.append(created_product_id)

    yield _delete_product
    for product_id in product_ids:
        data = {
            "selected[]": int(product_id)
        }
        response = requests.post(
            f"{url}/administration/index.php?route=catalog/product.delete&user_token={token}",
            data=data,
            cookies=cookies,
            headers={'Content-Type': 'application/x-www-form-urlencoded'})
        assert response.status_code == 200
