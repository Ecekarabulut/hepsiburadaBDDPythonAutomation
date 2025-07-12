from selenium.webdriver.common.by import By

# Placeholder for page object pattern
# You can expand this as needed

class LoginPage:
    USERNAME_INPUT = (By.ID, "txtUserName")
    PASSWORD_INPUT = (By.ID, "txtPassword")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
