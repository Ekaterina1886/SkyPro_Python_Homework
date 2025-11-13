from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop_total(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")


    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.go_to_cart()


    cart_page = CartPage(driver)
    items = cart_page.get_cart_items()
    expected_items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    assert items == expected_items, f"Ожидались {expected_items}, получено {items}"


    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form ("Ekaterina", "Petrova", "12345")


    total = checkout_page.get_total()
    assert total == "$58.29", f"Ожидалось $58.29, но получено: {total}"
