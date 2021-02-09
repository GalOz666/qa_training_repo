import selenium
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions


class BaseElement:

    def __init__(self, driver, selector, by=By.CSS_SELECTOR):
        self.selector = selector
        self.by = by
        self.driver = driver

    def get_element(self):
        return self.driver.find_element(by=self.by, value=self.selector)

    def wait_for_visibility(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((self.by, self.selector)))

    def is_element_visible(self, timeout=5):
        try:
            self.wait_for_visibility(timeout=timeout)
        except (TimeoutError, exceptions.WebDriverException):
            return False
        return True

    @property
    def text(self):
        return self.get_element()


class BaseButtonElement(BaseElement):

    def wait_for_clickable(self, time_sec=5):
        return WebDriverWait(self.driver, time_sec).until(
            expected_conditions.element_to_be_clickable((self.by, self.selector)))

    def click(self):
        self.wait_for_clickable()
        el = self.get_element()
        el.click()
        return self.go_to()

    def go_to(self):
        return self


class TextField(BaseButtonElement):

    def enter_text(self, text):
        el = self.get_element()
        el.send_keys(text)
