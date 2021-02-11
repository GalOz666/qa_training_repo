import pytest

from test_infra.base_classes import BaseTest


class BaseBasics(BaseTest):

    def helper(self):
        return True


class TestBasics(BaseBasics):

    def test_something(self, login_generic):
        home_btn = self.driver.find_element_by_css_selector('div[data-id="nav-bar-home-btn"]')
        assert self.helper(), "NOT TRUE!!"
        assert home_btn.is_displayed(), "home button doesn't appear after login!!!"
        assert "Dashboard".lower() in self.driver.current_url.lower(), "didn't go to proper url!!!!!!!!!"

    def test_login_page(self, setup_fixture):
        self.go_to_login_page()
        assert self.login_button.is_element_visible(timeout=10), "login button not visible!"
        workspace = self.login_page.click()
        assert workspace.toolbox.is_element_visible(), "login didn't lead to workspace!"


class TestMoreBasics(BaseBasics):

    @pytest.mark.parametrize('user, password', [('qa.automation+6669@powtoon.com', 'Powt00nP@ssw0rd!'),
                                                ('qa.automation+666@powtoon.com', 'Powt00nP@ssw0rd!')])
    def test_w_params(self, user, password, login_with_user):
        if 'qa' in user:
            print("you are from QA!")
        else:
            print("boris say you are opportunist!")

        # D R Y - DON'T REPEAT YOURSELF!
        #  K I S S - KEEP IT SIMPLE, STUPID!
