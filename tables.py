from logging import lastResort

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service("/Users/user/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/tables")

driver.maximize_window()

table1 = driver.find_element(By.ID, "table1")
rows = table1.find_elements(By.TAG_NAME, "tr")

print("full table data")
for row in rows:
    cells = row.find_elements(By.XPATH, ".//th|.//td")
    cell_text = [cell.text for cell in cells]
    print(cell_text)

#find last name is "Doe"

print("data for last name Doe")
data_rows = table1.find_elements(By.XPATH, ".//tbody/tr[1]")
for data_row in data_rows:
    lastname = data_row.find_element(By.XPATH, ".//td[1]").text
    if lastname == "Doe":
        values = [cell.text for cell in data_row.find_elements(By.TAG_NAME, "td")]
        print(values)
        break
