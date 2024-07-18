import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePageLocators:
    CONTENT_COLUMN = (By.XPATH, "//h3[text()='Featured']/../div[starts-with(@class,'row')]")
    CAROUSEL_ITEM = (By.XPATH, "//div[@class='carousel-item']")
    BUTTON_ADD_TO_CART = (By.XPATH, "//button[@title='Add to Cart']")
    ALERT_YOU_ADDED_PRODUCT = (By.XPATH, "//div[@id='alert']/div[text()=' Success: You have added ']")
    SHOPPING_CART = (By.XPATH, "//span[text()='Shopping Cart']")
    PRODUCT_URL = (By.XPATH, "//div[@class='content']//a")
    CURRENCY = (By.XPATH, "//div[@class='dropdown']//span[text()='Currency']")
    EUR = (By.XPATH, "//a[@href='EUR']")
    POUND_STERLING = (By.XPATH, "//a[@href='GBP']")
    PRICE_NEW = (By.XPATH, "//span[@class='price-new']")
    PRICE_OLD = (By.XPATH, "//span[@class='price-old']")
    PRICE_TAX = (By.XPATH, "//span[@class='price-tax']")


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_random_product_to_cart(self):
        element = self.find_elements_until_clickable(HomePageLocators.BUTTON_ADD_TO_CART)[0]
        self.click_element_with_js(element)

    def go_to_shopping_cart(self):
        shopping_cart = self.find_element(HomePageLocators.SHOPPING_CART)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", shopping_cart)
        self.wait_until_element_is_not_visible(HomePageLocators.ALERT_YOU_ADDED_PRODUCT)
        shopping_cart.click()

    def switch_currency_to_euro(self):
        self.find_element(HomePageLocators.CURRENCY).click()
        self.find_element(HomePageLocators.EUR).click()

    def switch_currency_to_pound_sterling(self):
        self.find_element(HomePageLocators.CURRENCY).click()
        self.find_element(HomePageLocators.POUND_STERLING).click()