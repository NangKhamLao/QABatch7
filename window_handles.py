import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/windows")



main_window = driver.current_window_handle

link = driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']")
link.click()

all_windows = driver.window_handles
time.sleep(4)

for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        break
        
print ("Current window text:", driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text)
time.sleep(4)

driver.switch_to.window(main_window)
print("back to main window:", driver.title)
time.sleep(2)



driver.close()
