from behave import then
from core.constants.login_message import VALID_LOGIN_SUCCESS_MESSAGE, LOGIN_SUCCESS_TITLE


@then('I verify login successfully message')
def verify_login_success_message(context):
    success_message = context.login_success_page.get_login_success_title()
    assert success_message == VALID_LOGIN_SUCCESS_MESSAGE

@then('I verify login successfully title')
def verify_login_success_title(context):
    success_title = context.login_success_page.get_login_success_title()
    assert success_title == LOGIN_SUCCESS_TITLE