from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch the browser')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()

@when('I open the login page')
def step_open_login(context):
    context.driver.get("https://example.com/login")

@when('I enter valid username and password')
def step_enter_credentials(context):
    context.driver.find_element(By.ID, "username").send_keys("admin")
    context.driver.find_element(By.ID, "password").send_keys("admin123")
    context.driver.find_element(By.ID, "login-button").click()

@then('I should be logged in successfully')
def step_verify_login(context):
    assert "Dashboard" in context.driver.title
    context.driver.quit()
