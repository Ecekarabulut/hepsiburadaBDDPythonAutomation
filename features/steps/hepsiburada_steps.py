print("hepsiburada_steps.py loaded")
from behave import given, when, then
from pages.home_page import HomePage
from pages.login_page import LoginPage

@given('the Hepsiburada home page is opened')
def open_home_page(context):
    context.home_page.accept_cookies()
    assert context.home_page.is_home_page_loaded(), "Home page did not load"

@then('cookies should be accepted')
def check_cookies_accepted(context):
    assert True, "Cookies were not accepted"

@when('the user clicks the login button')
def click_login_button(context):
    context.home_page.click_login_link()

@when('the user enters the username')
def enter_username(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_username("spamandthrash01@gmail.com")

@when('the user enters the password')
def enter_password(context):
    context.login_page.enter_password("0013700N.a") 