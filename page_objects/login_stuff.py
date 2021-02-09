from .base_object import BaseButtonElement, TextField


class LoginPage:

    def __init__(self, driver, validate=False):
        self.email_input = TextField(selector='[id="email_login"]', driver=driver)
        self.login_button = BaseButtonElement(selector='[data-label*="login"]', driver=driver)
        self.password_input = TextField(selector='[id="password_login"]', driver=driver)
        self.driver = driver
        if validate:
            assert '/login' in self.driver.current_url, "login url is wrong!"

    def enter_username_password(self, user, password):
        self.email_input.enter_text(text=user)
        self.password_input.enter_text(text=password)
