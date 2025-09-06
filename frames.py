import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")

driver.switch_to.frame("frame-middle")
print("middle frame text:", driver.find_element(By.ID, "content").text)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
print("frame bottom text:", driver.find_element(By.TAG_NAME, "body").text)