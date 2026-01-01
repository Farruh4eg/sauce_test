from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удается найти элемент с локатором {locator}"
        )


    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Не удается найти кликабельный элемент с локатором {locator}"
        )


    def go_to_site(self):
        return self.driver.get(self.base_url)


    def get_current_url(self):
        return self.driver.current_url
