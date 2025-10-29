from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop():

    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

 
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Ekaterina")
    driver.find_element(By.ID, "last-name").send_keys("Petrova")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    wait = WebDriverWait(driver, 10)
    total_text = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text

    assert "$58.29" in total_text, f"Ожидалось $58.29, получено: {total_text}"

    driver.quit()
