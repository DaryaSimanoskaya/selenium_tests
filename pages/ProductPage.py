from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductPageLocators:
    PRODUCT_IMAGE = (By.XPATH, "//div[@class='image magnific-popup']")
    QUANTITY = (By.XPATH, "//input[@name='quantity']")
    BUTTON_ADD_TO_CART = (By.XPATH, "//button[text()='Add to Cart']")
    BUTTON_GROUP_ADD_TO_WISH_LIST = (By.XPATH, "//form[@method='post']/div[@class='btn-group']")
    RATING = (By.XPATH, "//div[@class='rating']")


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
