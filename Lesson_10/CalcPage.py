from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    def __init__(self, driver) -> None:
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")    


    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
       
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажатие кнопки '{value}'")
    def click_button(self, value: str) -> None:
       
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    @allure.step("Ожидание результата '{expected_value}'")
    def wait_for_result(self, expected_value: str, timeout: int = 50) -> None:
        
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_value)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self) -> str:
    
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
