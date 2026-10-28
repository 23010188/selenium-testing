from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"


def login(driver, username, password=PASSWORD):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def cart_count(driver):
    badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    return int(badges[0].text) if badges else 0
