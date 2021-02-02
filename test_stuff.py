import time

import pytest
from drivers import chrome_driver
from page_objects.login_stuff import EmailInput, LoginBtn


class BaseTest:

    @pytest.fixture()
    def setup_fixture(self):
        self.driver = chrome_driver()
        self.driver.maximize_window()
        yield self.driver
        self.driver.close()
        self.driver.quit()

    @pytest.fixture()
    def login_generic(self, setup_fixture):
        self.driver.get("https://powtoon-newautotesting:newautotesting$1114@newautotesting.powtoon.com")
        login_button = LoginBtn
        login_button.click(driver=self.driver)
        email_input = EmailInput()
        email_input.wait_for_visibility()
        password_input = self.driver.find_element_by_css_selector('[id="password_login"]')
        email_input.enter_text(driver=self.driver, text='qa.automation+6669@powtoon.com')
        password_input.send_keys('Powt00nP@ssw0rd!')
        login_to_dashsboard_btn = self.driver.find_element_by_css_selector('[id="login_button"]')
        login_to_dashsboard_btn.click()
        time.sleep(5)  # wait 5 seconds!
        yield
        print("yay")


class TestBasics(BaseTest):

    def test_something(self, login_generic):
        home_btn = self.driver.find_element_by_css_selector('div[data-id="nav-bar-home-btn"]')
        assert home_btn.is_displayed(), "home button doesn't appear after login!!!"
        assert "Dashboard".lower() in self.driver.current_url.lower(), "didn't go to proper url!!!!!!!!!"
