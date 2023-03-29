from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

app_url = sys.argv[0]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

browser = webdriver.Chrome(options=chrome_options)

browser.get(app_url)

# Check that the application is up and running
assert browser.title == "React App1"
print("Application is up and running!")

browser.quit()
