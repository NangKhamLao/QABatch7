import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

fullname = driver.find_element(By.ID, "userName")
fullname.send_keys("Hla Hla")

form = driver.find_element(By.ID, "userForm")
form.submit()

submit_btn = driver.find_element(By.ID, "submit")
submit_btn.click()
