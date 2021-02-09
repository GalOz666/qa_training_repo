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
        if validate:
            assert '/login' in self.driver.current_url, "login url is wrong!"

    def enter_username_password(self, user, password):
        self.email_input.enter_text(text=user)
        self.password_input.enter_text(text=password)
