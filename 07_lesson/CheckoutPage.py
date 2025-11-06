from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
   
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first, last, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        
        wait = WebDriverWait(self.driver, 10)
        total_text = wait.until(EC.presence_of_element_located(self.TOTAL)).text
        return total_text.split(": ")[1]