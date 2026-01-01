import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Функционал авторизации")
class TestLogin:

    @allure.story("Успешная авторизация")
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.go_to_site()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in inventory_page.get_current_url(), "URL не соответствует ожидаемому"
        assert inventory_page.is_inventory_list_present(), "Список товаров не отображается"


    @allure.story("Логин с неверным паролем")
    def test_login_wrong_password(self, driver):
        login_page = LoginPage(driver)

        login_page.go_to_site()
        login_page.login("standard_user", "wrong_password")

        error_text = login_page.get_error_message()
        assert "Epic sadface: Username and password do not match any user in this service" in error_text


    @allure.story("Логин заблокированного пользователя")
    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)

        login_page.go_to_site()
        login_page.login("locked_out_user", "secret_sauce")

        error_text = login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error_text


    @allure.story("Логин с пустыми полями")
    def test_empty_fields(self, driver):
        login_page = LoginPage(driver)

        login_page.go_to_site()
        login_page.click_login_button()

        error_text = login_page.get_error_message()
        assert "Epic sadface: Username is required" in error_text


    @allure.story("Логин performance_glitch_user")
    @allure.description("Проверка авторизации с задержкой загрузки")
    def test_performance_glitch_user(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.go_to_site()
        login_page.login("performance_glitch_user", "secret_sauce")

        assert "inventory.html" in inventory_page.get_current_url()
        assert inventory_page.is_inventory_list_present()