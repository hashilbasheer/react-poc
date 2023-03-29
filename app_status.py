from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys

app_url = sys.argv[0]

caps = DesiredCapabilities.FIREFOX.copy()
caps["marionette"] = True
browser = webdriver.Firefox(capabilities=opts)

browser.get(app_url)

# Check that the application is up and running
assert browser.title == "React App1"
print("Application is up and running!")

browser.quit()
