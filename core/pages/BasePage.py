from core.utils.BrowserActions import BrowserActions
from core.utils.SeleniumWrapper import SeleniumWrapper

class BasePage:
    def __init__(self, driver):
        self.selenium = SeleniumWrapper(driver)
        self.browser = BrowserActions(driver)

    def get_title(self):
        return self.browser.get_page_title()

    def get_current_url(self):
        return self.browser.get_current_url()