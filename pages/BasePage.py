from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time_count=10):
        return WebDriverWait(self.driver, time_count).until(EC.presence_of_element_located(locator),
                                                            message=f"Can't find element by locator {locator}")

    def find_element_until_clickable(self, locator, time_count=10):
        return WebDriverWait(self.driver, time_count).until(EC.element_to_be_clickable(locator),
                                                            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time_count=10):
        return WebDriverWait(self.driver, time_count).until(EC.presence_of_all_elements_located(locator),
                                                            message=f"Can't find elements by locator {locator}")

    def wait_until_text_to_be_present_in_elements_attribute(self, locator, time_count=10):
        WebDriverWait(self.driver, time_count).until(EC.text_to_be_present_in_element_attribute(locator),
                                                     message=f"Can't find elements by locator {locator}")
        return self.driver.find_elements(*locator)

    def find_elements_until_clickable(self, locator, time_count=10):
        WebDriverWait(self.driver, time_count).until(EC.element_to_be_clickable(locator),
                                                     message=f"Can't find elements by locator {locator}")
        return self.driver.find_elements(*locator)

    def click_element_with_js(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_until_element_is_not_visible(self, locator, time_count=10):
        return WebDriverWait(self.driver, time_count).until(EC.invisibility_of_element(locator),
                                                            message=f"Element {locator} is still visible")


class BasePageLocators:
    MENU_NAVBAR = (By.CSS_SELECTOR, "#menu")
    SEARCH = (By.CSS_SELECTOR, "#search")
