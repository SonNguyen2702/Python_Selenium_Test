from selenium.webdriver.common.by import By

from core.constants.selenium_config import SHORT_WAIT
from core.constants.url import LOGIN_URL
from core.pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = LOGIN_URL  # Replace with actual login URL
        self.username_input = (By.XPATH, "//input[@name='userName']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//input[@type='submit']")
        self.error_message = (By.XPATH, "//input[@name='password']/../span")

    def open_login_page(self):
        self.browser.navigate_to(self.url)

    def input_username(self, username):
        self.selenium.input_text(self.username_input, username)

    def input_password(self, password):
        self.selenium.input_text(self.password_input, password)

    def click_login_button(self):
        self.selenium.click(self.login_button)

    def get_error_message(self):
        self.selenium.is_element_visible(self.error_message, timeout=SHORT_WAIT)
        return self.selenium.get_text(self.error_message)
