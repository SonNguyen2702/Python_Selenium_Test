from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def find_element(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator, timeout=None):
        element = self.find_element(locator, timeout)
        element.click()

    def input_text(self, locator, text, timeout=None):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=None):
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_visible(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_attribute(self, locator, attribute, timeout=None):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def is_selected(self, locator, timeout=None):
        element = self.find_element(locator, timeout)
        return element.is_selected()

