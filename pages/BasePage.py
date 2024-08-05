import time

from selenium.common import StaleElementReferenceException
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

    def wait_for_element(self, locator, time_count=10):
        WebDriverWait(self.driver, time_count).until(EC.presence_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")
        WebDriverWait(self.driver, time_count).until(EC.element_to_be_clickable(locator),
                                                     message=f"Can't find element by locator {locator}")
        return WebDriverWait(self.driver, time_count).until(EC.visibility_of_element_located(locator),
                                                            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time_count=10):
        return WebDriverWait(self.driver, time_count).until(EC.presence_of_all_elements_located(locator),
                                                            message=f"Can't find elements by locator {locator}")

    def click_element_with_js(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_until_element_is_not_visible(self, locator, time_count=10):
        return WebDriverWait(self.driver, time_count).until(EC.invisibility_of_element(locator),
                                                            message=f"Element {locator} is still visible")

    def wait_element_with_retry(self, locator, retries=3):
        for i in range(retries):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator),
                                                     message=f"Can't find element by locator {locator}")
                return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator),
                                                            message=f"Can't find element by locator {locator}")
            except StaleElementReferenceException:
                if i == retries - 1:
                    raise
                else:
                    time.sleep(1)

    def accept_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()


class BasePageLocators:
    MENU_NAVBAR = (By.CSS_SELECTOR, "#menu")
    SEARCH = (By.CSS_SELECTOR, "#search")
