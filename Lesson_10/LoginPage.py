import allure
from selenium.webdriver.common.by import By

class LoginPage:
    """Страница авторизации: https://www.saucedemo.com/"""
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver) -> None:
        self.driver = driver

    @allure.step("Открываем страницу авторизации")
    def open(self) -> None:
        self.driver.get(self.URL)

    
    @allure.step("Входим в систему как пользователь: {username}")
    def login(self, username:str, password:str) -> None:
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
