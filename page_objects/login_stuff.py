from .base_object import BaseButtonElement, TextField
from .workspace import WorkSpace


class LoginButton(BaseButtonElement):

    def __init__(self, driver):
        super().__init__(driver, selector='[data-label*="login"]')

    def go_to(self):
        return WorkSpace(self.driver)


class LoginPage:

    def __init__(self, driver, validate=False):
        self.email_input = TextField(selector='[id="email_login"]', driver=driver)
        self.password_input = TextField(selector='[id="password_login"]', driver=driver)
        self.driver = driver
        self.login_to_workspace = LoginButton(driver=driver)
        if validate:
            assert '/login' in self.driver.current_url, "login url is wrong!"

    def enter_username_password(self, user, password):
        self.email_input.enter_text(text=user)
        self.password_input.enter_text(text=password)


class LandingPage:

    class GotoLoginPage(BaseButtonElement):

        def __init__(self, driver):
            self.driver = driver
            super().__init__(driver, selector='[data-label="login"]')

        def go_to(self):
            return LoginPage(driver=self.driver)

    def __init__(self, driver, validate=False):
        self.driver = driver
        self.login_button = self.GotoLoginPage(driver=driver)
        if validate:
            assert 'powtoon' in self.driver.current_url
