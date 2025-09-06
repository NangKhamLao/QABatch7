import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_download_file(tmp_path):
    #use temporary folder
    download_dir = str(tmp_path)
    chrome_option = Options()
    chrome_option.add_experimental_option("prefs", {
        "download.default_directory":download_dir,
        "download.prompt_for_download":False,
        "safebrowsing.enabled":True
    })
    service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service, options = chrome_option)
    wait = WebDriverWait(driver, 30)
    # 2. enter username and password
    # 2.1 find username field and enter username
    driver.get("https://opensource-demo.orangehrmlive.com")

    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username.send_keys("Admin")
    # 2.2 find password filed and enter password
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("admin123")
    # 3. click login button
    loginbtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Login ']")))
    loginbtn.click()

    time.sleep(5)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/128")

    time.sleep(3)
    download_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-download']")))
    download_btn.click()

    time.sleep(3)
    #confirm file download
    download_file = os.listdir(download_dir)
    assert len(download_file)>0, "file download fail"

    #check file name and file type
    time.sleep(5)
    download_file_path = os.path.join(download_dir, download_file[0])
    print(f"File download successfully to:{download_file_path}")

    assert os.path.isfile(download_file_path), "download file is missing"

    driver.quit()


