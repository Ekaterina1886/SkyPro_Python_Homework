import pytest
from selenium import webdriver
from FormPage import FormPage
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Проверка формы")
@allure.story("Валидация подсветки полей")
@allure.title("Проверка подсветки при незаполненном Zip code")
def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    
    with allure.step("Открываем страницу формы"):
        form_page.open()
    
    with allure.step("Заполняем форму"):
        form_page.fill_form()
    
    with allure.step("Отправляем форму"):
        form_page.submit_form()
    
    with allure.step("Проверяем корректность подсветки полей"):
        form_page.check_form_submission()
    