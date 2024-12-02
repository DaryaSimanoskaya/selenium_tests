import logging
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logger = logging.getLogger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.logger.info(f"Initialized {self.__class__.__name__} with driver {driver}")

    def find_element(self, locator, time_count=10):
        self.logger.info(f"Finding element by locator: {locator}")
        element = WebDriverWait(self.driver, time_count).until(EC.presence_of_element_located(locator),
                                                               message=f"Can't find element by locator {locator}")
        self.logger.info(f"Found element {locator}")
        return element

    def find_element_until_clickable(self, locator, time_count=10):
        self.logger.info(f"Waiting for element to be clickable: {locator}")
        element = WebDriverWait(self.driver, time_count).until(EC.element_to_be_clickable(locator),
                                                               message=f"Can't find element by locator {locator}")
        self.logger.info(f"Element is clickable: {locator}")
        return element

    def wait_for_element(self, locator, time_count=10):
        self.logger.info(f"Waiting for element to be visible: {locator}")
        WebDriverWait(self.driver, time_count).until(EC.presence_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")
        WebDriverWait(self.driver, time_count).until(EC.element_to_be_clickable(locator),
                                                     message=f"Can't find element by locator {locator}")
        element = WebDriverWait(self.driver, time_count).until(EC.visibility_of_element_located(locator),
                                                               message=f"Can't find element by locator {locator}")
        self.logger.info(f"Element is visible: {locator}")
        return element

    def find_elements(self, locator, time_count=10):
        self.logger.info(f"Finding elements by locator: {locator}")
        elements = WebDriverWait(self.driver, time_count).until(EC.presence_of_all_elements_located(locator),
                                                                message=f"Can't find elements by locator {locator}")
        self.logger.info(f"Found elements: {locator}")
        return elements

    def click_element_with_js(self, element):
        self.logger.info(f"Clicking element with JS: {element}")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_until_element_is_not_visible(self, locator, time_count=10):
        self.logger.info(f"Waiting until element is not visible: {locator}")
        element = WebDriverWait(self.driver, time_count).until(EC.invisibility_of_element(locator),
                                                               message=f"Element {locator} is still visible")
        self.logger.info(f"Element is not visible: {locator}")
        return element

    def wait_element_with_retry(self, locator, retries=3):
        self.logger.info(f"Trying to find element with retry: {locator}")
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

    def element_is_exists(self, locator, time_count=2):
        self.logger.info(f"Checking if element exists: {locator}")
        try:
            WebDriverWait(self.driver, time_count).until(
                EC.presence_of_element_located(locator),
                message=f"Element not found: {locator}"
            )
            self.logger.info(f"Element exists: {locator}")
            return True
        except Exception as e:
            self.logger.warning(f"Element does not exist: {locator}. Exception: {e}")
            return False

    def accept_alert(self):
        self.logger.info("Waiting for and accepting alert")
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
        self.logger.info("Alert accepted")


class BasePageLocators:
    MENU_NAVBAR = (By.CSS_SELECTOR, "#menu")
    SEARCH = (By.CSS_SELECTOR, "#search")
