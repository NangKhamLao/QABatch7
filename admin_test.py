import time
from urllib.parse import uses_relative

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basic_function import driver


@pytest.mark.parametrize("username,password,confirm_pass,err_msg", [
    ("lily1","password1","password1"),
    ("lily","password1","password2",["Should be at least 5 characters"]),
    ("lily2","pass","pass",["Should have at least 7 characters"]),
    ("lily3","password","password",["Your password must contain minimum 1 number"]),
    ("lily4","password1","password2",["Passwords do not match"]),
    ("","","",["Required"])
])
def test_add_admin(login_as_admin,username, password, confirm_pass, err_msg):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)
    #1. click on admin tab
    admin_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Admin")))
    admin_tab.click()
    #2. click add button
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_btn.click()

    #3. enter user role
    user_role = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='User Role']/following::div[1]")))
    actions = ActionChains(driver)
    actions.move_to_element(user_role).click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    #4. enter employee name
    emp_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
    emp_name.send_keys("john")
    time.sleep(5)
    ActionChains(driver).move_to_element(emp_name).click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    #5. Status
    status = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Status']/following::div[1]")))
    ActionChains(driver).move_to_element(status).click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    #6. username
    user_name = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Username']/following::div[1]/input")))
    user_name.send_keys(username)
    #7. password
    pass_word = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Password']/following::div[1]/input")))
    pass_word.send_keys(password)
    #8. confirm password
    con_pass = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Confirm Password']/following::div[1]/input")))
    con_pass.send_keys(confirm_pass)
    #9. click save button
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    save_btn.click()

    if err_msg:
        for error in err_msg:
            msg = wait.until(EC.visibility_of_element_located((By.XPATH,f"//span[normalize-space()='{error}']")))
            assert msg.is_displayed(), "Expected error messages is not displayed"
    #10. confirm whether user added to system
    else:
        toast = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
        assert toast.is_displayed(),"Admin user not added"

def test_search_admin(login_as_admin):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)
    # 1. click on admin tab
    admin_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin")))
    admin_tab.click()

    user_name = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Username']/following::div[1]/input")))
    user_name.send_keys("lily1")

    form = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-form")))
    form.submit()

    confirm = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'lily1')]")))
    assert confirm.is_displayed(), "admin user is not found"

    edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")))
    edit_icon.click()

    change_pass = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']")))
    change_pass.click()

    ''' password
    comfirm_password
    assert edit successful '''

def test_delete_admin():
    #home work
    '''1. search admin user
    2. click delete button
    3. comfirm/cancel
    4. assert delete successfully '''
