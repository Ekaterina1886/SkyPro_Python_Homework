import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
   
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver) -> None:
        self.driver = driver

    @allure.step("Заполняем форму: {first} {last}, индекс {zip_code}")
    def fill_form(self, first:str, last:str, zip_code:str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Считываем итоговую сумму")
    def get_total(self) -> str:
        
        wait = WebDriverWait(self.driver, 10)
        total_text = wait.until(EC.presence_of_element_located(self.TOTAL)).text
        return total_text.split(": ")[1]