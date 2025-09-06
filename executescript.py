import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

#implicit wait
driver.implicitly_wait(10)

#explicit wait (base on condition)
#button is clickable or not?
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "button1"))).click()

checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

#check first checkbox
driver.execute_script("arguments[0].checked = true;", checkbox[0])
time.sleep(2)

#checkbox 2 uncheck
driver.execute_script("arguments[0].checked = false;", checkbox[1])

checkbox[1].click()
time.sleep(2)

