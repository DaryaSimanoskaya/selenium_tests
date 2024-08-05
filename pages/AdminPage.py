import time
from datetime import datetime

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AdminPageLocators:
    ADD_NEW_PRODUCT = (By.XPATH, "//a[@title='Add New']")
    PRODUCT_NAME = (By.XPATH, "//input[@placeholder='Product Name']")
    META_TAG_TITLE = (By.XPATH, "//input[@placeholder='Meta Tag Title']")
    MODEL = (By.XPATH, "//input[@placeholder='Model']")
    KEYWORD = (By.XPATH, "//input[@placeholder='Keyword']")
    SAVE_PRODUCT_BUTTON = (By.XPATH, "//button[@title='Save']")
    PRODUCT_DATA = (By.XPATH, "//a[text()='Data']")
    PRODUCT_SEO = (By.XPATH, "//a[text()='SEO']")
    ARROW_TO_LAST_PRODUCT = (By.XPATH, "//ul[@class='pagination']/li[last()]")
    LAST_PRODUCT = (By.XPATH, "//form[@id='form-product']//tbody//tr[last()]")
    CHECKBOX = (By.XPATH, "//form[@id='form-product']//tbody//tr[last()]//input")
    DELETE = (By.XPATH, "//button[@title='Delete']")
    ALERT_DELETE_PRODUCT_SUCCESS = (By.XPATH, "//div[text()=' Success: You have modified products! ']")


class AdminPage(BasePage):
    rand = f'{datetime.now():%Y%m%d-%H%M%S%z}'

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_product(self, name: str = f"{rand}", meta_tag: str = f"{rand}", model: str = f"{rand}",
                        keyword: str = f"{rand}"):
        self.find_element(AdminPageLocators.ADD_NEW_PRODUCT).click()
        self.find_element(AdminPageLocators.PRODUCT_NAME).send_keys(name)
        self.find_element(AdminPageLocators.META_TAG_TITLE).send_keys(meta_tag)
        self.find_element(AdminPageLocators.PRODUCT_DATA).click()
        self.find_element(AdminPageLocators.MODEL).send_keys(model)
        self.find_element(AdminPageLocators.PRODUCT_SEO).click()
        self.find_element(AdminPageLocators.KEYWORD).send_keys(keyword)
        self.find_element(AdminPageLocators.SAVE_PRODUCT_BUTTON).click()

    def go_to_last_product(self):
        last_product = self.find_element(AdminPageLocators.ARROW_TO_LAST_PRODUCT)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_product)
        self.wait_for_element(AdminPageLocators.ARROW_TO_LAST_PRODUCT).click()

    def delete_product(self, value):
        checkbox = (By.XPATH, f"//input[@value='{value}']")
        self.find_element(checkbox).click()
        self.find_element(AdminPageLocators.DELETE).click()
        self.accept_alert()