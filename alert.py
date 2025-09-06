import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
js_alert.click()

alert = driver.switch_to.alert
alert.accept()

js_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
js_confirm.click()

confirm_alert = driver.switch_to.alert
confirm_alert.dismiss()
time.sleep(2)


js_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
js_prompt.click()
time.sleep(2)


prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("55555")
prompt_alert.accept()
time.sleep(2)

