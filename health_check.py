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

# Check that the application is up and running
assert browser.title == "React App1"
print("Application is up and running!")


driver.quit()
