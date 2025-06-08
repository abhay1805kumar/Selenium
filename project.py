from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
query = "laptop"
file = 0

# Create directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

for i in range(1, 5):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}")
    time.sleep(3)  # Wait for the page to load

    # Find all product elements using the class name
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"Page {i}: Found {len(elems)} items")

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1

time.sleep(6)
driver.quit()

