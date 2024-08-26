import time

import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AdminLoginPageLocators:
    USERNAME = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN = (By.XPATH, "//button[text()=' Login']")
    INFO_PLEASE_ENTER_CREDENTIALS = (By.XPATH, "//div[text()=' Please enter your login details.']")
    NAVIGATION = (By.CSS_SELECTOR, "#navigation")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    EXTENSIONS = (By.CSS_SELECTOR, "#menu-extension")
    DESIGN = (By.CSS_SELECTOR, "#menu-design")
    SALES = (By.CSS_SELECTOR, "#menu-sale")
    CUSTOMERS = (By.CSS_SELECTOR, "#menu-customer")
    MARKETING = (By.CSS_SELECTOR, "#menu-marketing")
    SYSTEM = (By.CSS_SELECTOR, "#menu-system")
    REPORTS = (By.CSS_SELECTOR, "#menu-report")
    WORD_MAP = (By.XPATH, "//div[text()=' World Map']")
    SALES_ANALYTICS = (By.XPATH, "//div[text()[contains(.,'Sales Analytics')]]")
    LOGOUT = (By.XPATH, "//span[text()='Logout']")



class AdminLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Set login username")
    def set_login(self, username):
        self.find_element(AdminLoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.find_element(AdminLoginPageLocators.PASSWORD).send_keys(password)

    @allure.step("Click login button")
    def login(self):
        self.find_element(AdminLoginPageLocators.LOGIN).click()

    @allure.step("Click logout button")
    def logout(self):
        self.find_element(AdminLoginPageLocators.LOGOUT).click()

    @allure.step("Get admin token and cookies from URL: {url}")
    def get_admin_token_and_cookies(self, url):
        self.driver.get(f"{url}/administration/index.php?route=common/login")
        self.driver.find_element(By.ID, "input-username").send_keys("admin")
        self.driver.find_element(By.ID, "input-password").send_keys("admin")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        current_url = self.driver.current_url
        token = current_url.split("user_token=")[-1]
        cookies = self.driver.get_cookies()
        session_cookies = {cookie['name']: cookie['value'] for cookie in cookies}
        return token, session_cookies
