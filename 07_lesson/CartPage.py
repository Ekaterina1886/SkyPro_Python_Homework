from selenium.webdriver.common.by import By

class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
