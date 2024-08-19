from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegistrationPageLocators:
    FIRSTNAME = (By.XPATH, "//input[@name='firstname']")
    LASTNAME = (By.XPATH, "//input[@name='lastname']")
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    SUBSCRIBE = (By.XPATH, "//label[text()='Subscribe']/..//input[@type='checkbox']")
    MY_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    REGISTER = (By.XPATH, "//a[text()='Register']")
    PRIVACY_POLICY = (By.XPATH, "//label[text()='I have read and agree to the ']/..//input[@type='checkbox']")
    CONTINUE = (By.XPATH, "//button[text()='Continue']")
    END_REGISTRATION = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")


class RegistrationPage(BasePage):
    rand = f'{datetime.now():%Y%m%d-%H%M%S%z}'

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Register a new user with details: Firstname: {firstname}, Lastname: {lastname}, Email: {email}")
    def register_new_user(self, firstname: str = f"Firstname-{rand}",
                          lastname: str = f"Lastname-{rand}",
                          email: str = f"test-email{rand}@mail.ru",
                          password: str = rand):
        self.find_element(RegistrationPageLocators.MY_ACCOUNT).click()
        self.find_element(RegistrationPageLocators.REGISTER).click()
        self.find_element(RegistrationPageLocators.FIRSTNAME).send_keys(firstname)
        self.find_element(RegistrationPageLocators.LASTNAME).send_keys(lastname)
        self.find_element(RegistrationPageLocators.EMAIL).send_keys(email)
        self.find_element(RegistrationPageLocators.PASSWORD).send_keys(password)
        self.find_element(RegistrationPageLocators.SUBSCRIBE).click()
        self.find_element(RegistrationPageLocators.PRIVACY_POLICY).click()
        self.find_element(RegistrationPageLocators.CONTINUE).click()
