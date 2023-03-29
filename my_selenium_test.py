import sys
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

app_url = sys.argv[0]
driver_path = /usr/bin/google-chrome

caps = DesiredCapabilities.CHROME.copy()
caps["goog:loggingPrefs"] = {"browser": "ALL"}

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-browser-side-navigation')

browser = webdriver.Chrome(options=options, executable_path=driver_path, desired_capabilities=caps)

def check_application_status():
    try:
        browser.get(app_url)
        while browser.execute_script('return document.readyState') != 'complete':
            time.sleep(1)
        assert browser.title == "React App1"
        print("Application is up and running!")
    except Exception as e:
        print("Error: {}".format(str(e)))

check_application_status()
browser.quit()
