from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/")
print(driver.title)
print(driver.current_url)
driver.close()
