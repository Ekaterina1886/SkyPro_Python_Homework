from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation_safari():
    
    driver = webdriver.Safari()
    driver.maximize_window()

    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

       
        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "", 
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for name, value in data.items():
            field = driver.find_element(By.NAME, name)
            field.clear()
            field.send_keys(value)

       
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

     
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert"))
        )

        
        inputs = driver.find_elements(By.CSS_SELECTOR, "input")

        for field in inputs:
            name = field.get_attribute("name")
            border_color = field.value_of_css_property("border-color")

            if name == "zip-code":
                
                assert "rgb(132, 32, 41)" in border_color or "red" in border_color, \
                    f"Ожидался красный бордер у zip-code, получено: {border_color}"
            else:
                
                assert "rgb(33, 136, 56)" in border_color or "green" in border_color, \
                    f"Поле '{name}' не подсвечено зелёным, получено: {border_color}"

    finally:
       
        driver.quit()