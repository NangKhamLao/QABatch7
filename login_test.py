import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 30)
    #1. Open orangeHRM webpage
    driver.refresh()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    #2. enter username and password
    #2.1 find username field and enter username
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username.send_keys("Admin")
    #2.2 find password filed and enter password
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("admin123")
    #3. click login button
    loginbtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Login ']")))
    loginbtn.click()
    #4. confirm login
    driver.refresh()
    assert "dashboard" in driver.current_url, "Login Failed"

#testing မစခင်မှာ လုပ်ထားရမယ့် အလုပ်ကို pytest.fixture ကိုသုံးပြီး setup လုပ်ထားလို့ရ
#pytest.fixture()
#pytest.fixture(scope="function") --> run before each test
#pytest.fixture(scope="class") --> run before test class
#pytest.fixture(scope="module") --> runs once per test file
#pytest.fixture(scope="session") --> runs once for the whole test


