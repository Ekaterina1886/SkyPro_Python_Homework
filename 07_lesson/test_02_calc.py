import pytest
from selenium import webdriver
from CalcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome() 
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calc_with_delay(driver):
    calc = CalcPage(driver)
    calc.open()

    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    calc.wait_for_result("15", timeout=50)

    result = calc.get_result()
    assert result == "15", f"Ожидалось 15, но получено: {result}"