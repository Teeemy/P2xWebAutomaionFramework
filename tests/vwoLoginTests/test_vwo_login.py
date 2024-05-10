import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginpage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage


# we can add Assertions
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - Vwo App Negative Test Case")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(email="adminadmin@gmail.com", password="admin")

    time.sleep(5)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - Vwo App Positive Test Case")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(email="onibonojemariam@gmail.com", password="Oyinkan@32")
    time.sleep(10)
    dashboardPage = DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "Mariam Temitope" in dashboardPage.user_logged_in_text()

    assert True == True
