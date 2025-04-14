from selenium.webdriver.common.by import By
from core.pages.BasePage import BasePage

class LoginSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.success_login_message = (By.XPATH, "//td[@valign='top']//h3")

    def get_login_success_title(self):
        return self.get_title()

    def get_login_success_message(self):
        return self.selenium.get_text(self.success_login_message)