from selenium.webdriver.common.by import By
from utils import login


def test_TC01_login_success(driver):
    login(driver, "standard_user")
    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"


def test_TC02_login_wrong_password(driver):
    login(driver, "standard_user", "sai_mat_khau")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "do not match" in error


def test_TC03_login_locked_user(driver):
    login(driver, "locked_out_user")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked out" in error


def test_TC04_login_empty_fields(driver):
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username is required" in error
