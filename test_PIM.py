import os.path

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basic_function import driver


def test_add_employee(login_as_admin):
    driver = login_as_admin
    wait = WebDriverWait(driver,30)
    pim_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM")))
    pim_tab.click()

    add_pim = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Employee']")))
    add_pim.click()

    #firstname
    firstname = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
    firstname.send_keys("Ei")

    #middlename
    middlename = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Middle Name']")))
    middlename.send_keys("Ei")

    #lastname
    lastname = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Last Name']")))
    lastname.send_keys("Khaing")

    '''file upload
    1. find >>input type = file
    2. abspath >> os.path.abspath(file location)
    3. send_keys'''

    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    img_source = os.path.abspath("./resources/1.png")
    file_input.send_keys(img_source)

    #confirm file upload
    upload_pic = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"employee-image"))).get_attribute("src")
    assert "/web/images/default-photo.png" not in upload_pic, "image upload fail"

    toogle = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")))
    toogle.click()
    #username
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Username']/following::div[1]/input"))).send_keys("EiEiI")

    #enable
    enable = wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='Enabled']")))
    enable.click()
    #password
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Password']/following::div[1]/input"))).send_keys("Admin123")

    #confirm pass
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Confirm Password']/following::div[1]/input"))).send_keys("Admin123")

    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    save_btn.click()

    toast = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
    assert toast.is_displayed(), "employee not added"

    # driver license no
    licenseNo = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'License Number')]/following::div/input")))
    licenseNo.clear()
    licenseNo.send_keys("OK0011011")

    # license expire date
    license_exp = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='License Expiry Date']/following::input[1]")))
    license_exp.clear()
    license_exp.send_keys("2029-01-01")

    # nationality
    dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Nationality']/following::div")))
    dropdown.click()
    option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() ='Japanese']"))
    )
    option.click()

    # marital status
    marital_status = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Marital Status']/following::div[1]")))
    ActionChains(driver).move_to_element(marital_status).click().send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.ENTER).perform()

    # date of birth
    dob = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Date of Birth']/following::input[1]")))
    dob.clear()
    dob.send_keys("1994-01-01")

    # gender
    # female radio
    female_radio = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Female']")))
    if not female_radio.is_selected():
        female_radio.click()

    #attachment
    file_input1 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    img_source1 = os.path.abspath("./resources/Pytest Flag.pdf")
    file_input1.send_keys(img_source1)

    #save button
    wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']"))).click()


    toast1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
    assert toast1.is_displayed(), "employee not updated"

    #confirm add attachement
    file_name = wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Pytest Flag.pdf')]")))
    assert file_name.is_displayed(), "file not uploaded."






