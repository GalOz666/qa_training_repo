
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseElement:

    def __init__(self, selector, by=By.CSS_SELECTOR):
        self.selector = selector
        self.by = by

    def wait_for_visibility(self, driver, time_sec=5):
        return WebDriverWait(driver, time_sec).until(
            expected_conditions.visibility_of_element_located((self.by, self.selector)))


class BaseButtonElement(BaseElement):

    def wait_for_clickable(self, driver, time_sec=5):
        return WebDriverWait(driver, time_sec).until(
            expected_conditions.element_to_be_clickable((self.by, self.selector)))

    def click(self, driver):
        self.wait_for_clickable(driver)
        el = driver.find_element(self.by, self.selector)
        el.click()


class TextField(BaseButtonElement):

    def enter_text(self, driver, text):
        el = driver.find_element()
        el.send_keys(text)
