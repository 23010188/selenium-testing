import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import BASE_URL, login


@pytest.fixture
def driver():
    options = Options()
    # Bỏ comment dòng dưới nếu muốn chạy không mở cửa sổ trình duyệt
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    # Tắt popup cảnh báo mật khẩu của Chrome (popup này hay chặn thao tác click)
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    drv = webdriver.Chrome(options=options)  # Selenium 4 tự tải ChromeDriver
    drv.implicitly_wait(5)
    drv.get(BASE_URL)
    yield drv
    drv.quit()


@pytest.fixture
def logged_in(driver):
    login(driver, "standard_user")
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Tự chụp màn hình khi test bị fail."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver") or item.funcargs.get("logged_in")
        if drv:
            os.makedirs("screenshots", exist_ok=True)
            drv.save_screenshot(f"screenshots/FAIL_{item.name}.png")
