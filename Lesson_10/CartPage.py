import allure
from selenium.webdriver.common.by import By

class CartPage:
    """Переходит к оформлению заказа"""
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver) -> None:
        self.driver = driver

    @allure.step("Получаем список товаров в корзине")
    def get_cart_items(self) ->str:
        
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.text for item in items]

    @allure.step("Нажимаем кнопку Checkout")
    def click_checkout(self) -> None:
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
