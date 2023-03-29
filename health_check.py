from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/"

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

try:
    # Wait for an element to appear on the page
    element_present = EC.presence_of_element_located((By.ID, "Welcome to VOLVO SALES COCKPIT with GH_RUN_NUMBER"))
    WebDriverWait(driver, timeout=30).until(element_present)
    print(f"{url} is accessible and the 'my-element' element was found.")
except TimeoutError:
    print(f"{url} is accessible but the 'my-element' element was not found.")

driver.quit()
