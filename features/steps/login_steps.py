from behave import given, when, then
from core.constants.login_message import INVALID_LOGIN_ERROR_MESSAGE

@given('I open the login page')
def open_login_page(context):
    context.login_page.open_login_page()

@when('I enter username "{username}"')
def enter_username(context, username):
    if username == "None":
        username = ""
    context.login_page.input_username(username)

@when('I enter password "{password}"')
def enter_password(context, password):
    if password == "None":
        password = ""
    context.login_page.input_password(password)

@when('I press submit button')
def click_submit(context):
    context.login_page.click_login_button()

@then('I verify login failed error message')
def verify_error_message(context):
    error_message = context.login_page.get_error_message()
    print(error_message)
    assert error_message == INVALID_LOGIN_ERROR_MESSAGE