from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=37NXMQR1TS601&sprefix=%2Caps%2C222&ref=nb_sb_ss_recent_1_0_recent")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.get_attribute("outerHTML"))

time.sleep(8)
driver.close()