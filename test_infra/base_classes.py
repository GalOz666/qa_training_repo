import time

import pytest

from drivers import chrome_driver
from page_objects.login_stuff import LoginPage


class BaseTest:

    @pytest.fixture()
    def setup_fixture(self):
        self.driver = chrome_driver()
        self.driver.maximize_window()
        yield self.driver
        self.driver.close()
        self.driver.quit()

    @pytest.fixture()
    def login_generic(self, setup_fixture, user="qa.automation+6669@powtoon.com", password='Powt00nP@ssw0rd!'):
        self.go_to_login_page()
        self.login_page.enter_username_password(user, password)
        login_to_dashsboard_btn = self.driver.find_element_by_css_selector('[id="login_button"]')
        login_to_dashsboard_btn.click()
        time.sleep(5)  # wait 5 seconds!
        yield
        print("yay")

    def go_to_login_page(self):
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://powtoon-newautotesting:newautotesting$1114@newautotesting.powtoon.com")
        self.login_page.login_button.click()
        self.login_page.email_input.wait_for_visibility()
        self.login_button = self.login_page.login_button
        self.email_input = self.login_page.email_input
        self.password_input = self.login_page.password_input
        return self.login_button, self.email_input, self.password_input
