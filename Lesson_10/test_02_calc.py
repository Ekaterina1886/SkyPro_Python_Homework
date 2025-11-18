import allure
import pytest
from selenium import webdriver
from CalcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome() 
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Проверка калькулятора c задержкой")
@allure.description("Tест проверяет корректность работы калькулятора")
def test_calc_with_delay(driver):
    calc = CalcPage(driver)
    
    with allure.step("Открываем страницу калькулятора"):
        calc.open()

    with allure.step("Устанавливаем задержку"):
        calc.set_delay(45)

    with allure.step("Выполняем выражение 7 + 8 ="):
        calc.click_button("7")
        calc.click_button("+")
        calc.click_button("8")
        calc.click_button("=")

    with allure.step("Ожидаем появление результата 15"):
        calc.wait_for_result("15", timeout=50)

    with allure.step("Проверяем результат"):
        result = calc.get_result()
        assert result == "15", f"Ожидалось 15, но получено: {result}"