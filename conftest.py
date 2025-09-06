import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def setup_teardown():
    service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 30)
    # 1. Open orangeHRM webpage
    driver.refresh()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    yield driver


@pytest.fixture()
def login_as_admin(setup_teardown):
    driver = setup_teardown
    wait = WebDriverWait(driver,30)
    # 2. enter username and password
    # 2.1 find username field and enter username
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username.send_keys("Admin")
    # 2.2 find password filed and enter password
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("admin123")
    # 3. click login button
    loginbtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Login ']")))
    loginbtn.click()
    # 4. confirm login
    driver.refresh()
    assert "dashboard" in driver.current_url, "Login Failed"
    return driver


