from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CatalogPageLocators:
    LEFT_SIDE_BAR_DESKTOPS = (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'Desktops')]]")
    LEFT_SIDE_BAR_LAPTOPS_AND_NOTEBOOKS = \
        (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'Laptops & Notebooks')]]")
    LEFT_SIDE_BAR_COMPONENTS = (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'Components')]]")
    LEFT_SIDE_BAR_TABLETS = (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'Tablets')]]")
    LEFT_SIDE_BAR_SOFTWARE = (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'Software')]]")
    LEFT_SIDE_BAR_PHONES_AND_PDAS = (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'Phones & PDAs')]]")
    LEFT_SIDE_BAR_CAMERAS = (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'Cameras')]]")
    LEFT_SIDE_BAR_MP3_PLAYERS = (By.XPATH, "//aside[@id='column-left']//a[text()[starts-with(.,'MP3 Players')]]")


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
