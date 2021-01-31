import time

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    desired_capabilities = {'goog:loggingPrefs': {'performance': 'ALL', 'browser': 'ALL'}}
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                              options=options, desired_capabilities=desired_capabilities)
    return driver


class BaseBasics:

    def add(self, num1: int, num2: int):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2


class TestBasics(BaseBasics):

    @pytest.fixture()
    def setup_fixture(self):
        self.driver = chrome_driver()
        self.driver.maximize_window()
        yield self.driver
        self.driver.close()
        self.driver.quit()

    @pytest.fixture()
    def login_generic(self, setup_fixture):
        to_login_page_btn = '[data-label*="login"]'
        self.driver.get("https://powtoon-newautotesting:newautotesting$1114@newautotesting.powtoon.com")
        login_button = self.driver.find_element_by_css_selector(to_login_page_btn)
        login_button.click()
        time.sleep(5)
        email_input = self.driver.find_element_by_css_selector('[id="email_login"]')
        password_input = self.driver.find_element_by_css_selector('[id="password_login"]')
        email_input.send_keys('qa.automation+6669@powtoon.com')
        password_input.send_keys('Powt00nP@ssw0rd!')
        login_to_dashsboard_btn = self.driver.find_element_by_css_selector('[id="login_button"]')
        login_to_dashsboard_btn.click()
        time.sleep(5)
        yield
        print("yay")

    def test_something(self, login_generic):
        home_btn = self.driver.find_element_by_css_selector('div[data-id="nav-bar-home-btn"]')
        assert home_btn.is_displayed(), "home button doesn't appear after login!!!"
        assert "Dashboard".lower() in self.driver.current_url.lower(), "didn't go to proper url!!!!!!!!!"

