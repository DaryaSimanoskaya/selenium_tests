from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CartPageLocators:
    ADDED_PRODUCT_URL = (By.XPATH, "//div[@id='shopping-cart']//a")
    QUANTITY = (By.XPATH, "//input[@name='quantity']")
    BUTTON_REMOVE = (By.XPATH, "//div[@class='input-group']/button[@title='Remove']")
    EMPTY_CART = (By.XPATH, "//p[text()='Your shopping cart is empty!']")


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def remove_first_item_from_cart(self):
        self.find_elements(CartPageLocators.BUTTON_REMOVE)[0].click()
