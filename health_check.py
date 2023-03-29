from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

chrome_driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver")

driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)

url = "https://www.example.com"

driver.get(url)

try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "my-element")))
    print("URL is accessible.")
except:
    print("URL is not accessible.")

driver.quit()
