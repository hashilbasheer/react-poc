from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/")
print(driver.page_source)
driver.quit()
