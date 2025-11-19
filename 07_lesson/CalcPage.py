from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")    


    def set_delay(self, seconds: int):
       
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, value: str):
       
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def wait_for_result(self, expected_value: str, timeout: int = 50):
        
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_value)
        )

    def get_result(self) -> str:
    
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
