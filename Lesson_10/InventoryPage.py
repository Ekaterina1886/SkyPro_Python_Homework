import allure
from selenium.webdriver.common.by import By

class InventoryPage:
    """Каталог товаров"""
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver) -> None:
        self.driver = driver

    @allure.step("Добавляем в корзину товар: {item_name}")
    def add_to_cart(self, item_name:str) -> None:
        
        locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        self.driver.find_element(*locator).click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self) -> None:
        self.driver.find_element(*self.CART_LINK).click()
