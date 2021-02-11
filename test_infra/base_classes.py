import time

import pytest

from drivers import chrome_driver
from page_objects.login_stuff import LoginPage, LandingPage


class BaseTest:

    @pytest.fixture
    def setup_fixture(self):
        self.driver = chrome_driver()
        self.driver.maximize_window()
        self.driver.get("https://powtoon-newautotesting:newautotesting$1114@newautotesting.powtoon.com")
        yield self.driver
        self.driver.close()
        self.driver.quit()

    @pytest.fixture
    def login_generic(self, setup_fixture):
        self.full_login_process()
        yield
        print("yay")

    @pytest.fixture
    def login_with_user(self, setup_fixture, user, password):
        self.full_login_process(user=user, password=password)

    def go_to_login_page(self):
        self.landing_page = LandingPage(self.driver)
        self.login_page = self.landing_page.login_button.click()
        self.login_page.email_input.wait_for_visibility(timeout=10)
        self.login_button = self.login_page
        self.email_input = self.login_page.email_input
        self.password_input = self.login_page.password_input
        return self.login_button, self.email_input, self.password_input

    def full_login_process(self, user="qa.automation+6669@powtoon.com", password='Powt00nP@ssw0rd!'):
        self.go_to_login_page()
        self.login_page.enter_username_password(user, password)
        login_to_dashsboard_btn = self.driver.find_element_by_css_selector('[id="login_button"]')
        login_to_dashsboard_btn.click()
        time.sleep(5)  # wait 5 seconds!
