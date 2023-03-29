import sys
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

app_url = sys.argv[0]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

browser = webdriver.Chrome(chrome_options=chrome_options)

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
