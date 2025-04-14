from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from core.pages.LoginPage import LoginPage
from core.pages.LoginSuccessPage import LoginSuccessPage


def before_all(context):
    chrome_options = Options()
    chrome_driver_path = ChromeDriverManager().install()
    chrome_options.add_argument(f'webdriver.chrome.driver={chrome_driver_path}')
    context.driver = webdriver.Chrome(options=chrome_options)
    context.login_page=LoginPage(driver=context.driver)
    context.login_success_page=LoginSuccessPage(driver=context.driver)

def after_all(context):
    context.driver.quit()

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()