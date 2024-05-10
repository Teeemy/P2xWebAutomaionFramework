# dashboard and loginpage are page class


# page class consists of
# 1. Page locators and 2. Page Actions
# it also contains webdriver initialization
# we can also create custom functions
# there is no assertions in page object class

# Login Page Class

# Responsibility is to
# get email and send keys - email
# # get password and send keys - email
# # click the submit button and navigate to dashboard Page
# for Invalid test case -> error message
# Forgot password


# Page Class

# Page Locators
# Page Actions
# WebDriver Init
# Custom Functions
# No assertions(in Page Object Class)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create a class
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # page locators

    email = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    # free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")

    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH,
    # "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*
    # [name()='svg']")

    # page Actions

    def get_email(self):
        return self.driver.find_element(*LoginPage.email)  # * means current class.email here

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trail(self):
        return self.driver.find_element(*LoginPage.free_trail)

    # main Action is here
    # Page Action

    def login_to_vwo(self, email, password):
        self.get_email().send_keys(email)
        self.get_password().send_keys(password)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text
