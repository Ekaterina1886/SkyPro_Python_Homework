from selenium.webdriver.common.by import By

class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name):
        
        locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
