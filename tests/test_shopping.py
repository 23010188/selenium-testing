from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import BASE_URL, cart_count


def test_TC05_add_to_cart(logged_in):
    d = logged_in
    d.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    assert cart_count(d) == 1
    d.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert d.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"


def test_TC06_remove_from_cart(logged_in):
    d = logged_in
    d.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    d.find_element(By.ID, "remove-sauce-labs-backpack").click()
    assert cart_count(d) == 0


def test_TC07_sort_price_low_to_high(logged_in):
    d = logged_in
    Select(d.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")
    prices = [float(p.text.replace("$", ""))
              for p in d.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert prices == sorted(prices)


def test_TC08_checkout(logged_in):
    d = logged_in
    d.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    d.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    d.find_element(By.ID, "checkout").click()
    d.find_element(By.ID, "first-name").send_keys("Tuyen")
    d.find_element(By.ID, "last-name").send_keys("Hoang")
    d.find_element(By.ID, "postal-code").send_keys("700000")
    d.find_element(By.ID, "continue").click()
    d.find_element(By.ID, "finish").click()
    assert d.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"


def test_TC09_logout(logged_in):
    d = logged_in
    d.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(d, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    assert d.current_url == BASE_URL
    assert d.find_element(By.ID, "login-button").is_displayed()
