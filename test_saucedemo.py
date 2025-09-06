import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("username,password, expected", [
    ("standard_user", "secret_sauce", True), #test case pass
    ("locked_out_user","secret_sauce", False), #expected fail
    ("problem_user","secret_sauce",True),
    ("performance_glitch_user","secret_sauce",True),
    ("invalid_user","invalid_password",False)
])
def test_login(username,password,expected):
    service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    #1. Open orangeHRM webpage
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    #2. enter username and password
    #2.1 find username field and enter username
    Username = wait.until(EC.presence_of_element_located((By.NAME, "user-name")))
    Username.send_keys(username)
    #2.2 find password filed and enter password
    Password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    Password.send_keys(password)
    #3. click login button
    loginbtn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    loginbtn.click()
    #4. confirm login
    if expected:
        assert "inventory" in driver.current_url, "Login Failed"
    else:
        err_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        assert "Epic sadface" in err_msg.text, "Login Successful"

    driver.quit()

