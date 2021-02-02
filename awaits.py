from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def wait_for_visibility_css(driver, time_sec, css):
    return WebDriverWait(driver, time_sec).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css)))
