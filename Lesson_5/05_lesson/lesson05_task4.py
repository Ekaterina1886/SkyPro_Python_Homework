from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get ("http://the-internet.herokuapp.com/login")
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

username_input = driver.find_element(By.CSS_SELECTOR, "input#username")
username_input.send_keys(USERNAME)

password_input = driver.find_element(By.CSS_SELECTOR, "input#password")
password_input.send_keys(PASSWORD)

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")


print("Текст зеленой плашки:", success_message.text.strip())

driver.quit()