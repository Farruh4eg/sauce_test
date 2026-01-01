from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Ввод имени пользователя")
    def enter_username(self, username):
        self.find_element(self.USERNAME).send_keys(username)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.find_element(self.PASSWORD).send_keys(password)

    @allure.step("Нажатие кнопки логина")
    def click_login_button(self):
        self.find_clickable_element(self.LOGIN_BUTTON).click()

    @allure.step("Получение текста ошибки")
    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    @allure.step("Полный процесс авторизации")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()