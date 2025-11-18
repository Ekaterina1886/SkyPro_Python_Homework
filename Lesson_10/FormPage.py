import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    def __init__(self, driver) -> None: 
        
        """сохраняет драйвер и создаёт объект страницы"""

        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открываем страницу формы")
    def open(self) -> None:
        """Открывает страницу формы"""
        
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    @allure.step("Заполняем форму всеми значениями")
    def fill_form(self) -> None:
        """Заполняет все поля значениями из self.fields"""
        
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Отправляем форму")
    def submit_form(self):
        """Нажимает кнопку Submit"""
        
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Получаем класс поля '{field_id}'")
    def get_field_class(self, field_id:str) -> str:
        """Возвращает значение атрибута class для поля"""
        
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверяем, что ZIP-код подсвечен красным")
    def check_zip_code_error(self) -> bool:
        """Проверяет, подсвечено ли поле ZIP-кода красным"""
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверяем, что все обязательные поля подсвечены зелёным")
    def check_fields_success(self) ->bool:
        """Проверяет, что остальные поля подсвечены зелёным"""
    
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверяем результаты отправки формы")
    def check_form_submission(self) -> None:
        """Проводит итоговую проверку (ZIP — ошибка, остальные — success)"""
        assert self.check_zip_code_error()
        assert self.check_fields_success()