from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegistrationPageLocators:
    FIRSTNAME = (By.XPATH, "//input[@name='firstname']")
    LASTNAME = (By.XPATH, "//input[@name='lastname']")
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    SUBSCRIBE = (By.XPATH, "//label[text()='Subscribe']/..//input[@type='checkbox']")


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
