from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BrowserActions:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def navigate_to(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def maximize_window(self):
        self.driver.maximize_window()

    def implicit_wait(self, seconds):
        self.driver.implicitly_wait(seconds)