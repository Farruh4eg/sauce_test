from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    TITLE = (By.CLASS_NAME, "title")

    def is_inventory_list_present(self):
        return self.find_element(self.INVENTORY_LIST) is not None