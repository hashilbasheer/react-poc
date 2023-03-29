from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the application URL
driver.get('http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/')

# Check if the application is healthy by looking for a specific element on the page
try:
    element = driver.find_element(By.XPATH, "//div[@id='health-check']//span[text()='VOLVO']")
    print("Application is healthy")
except:
    print("Application is not healthy")

# Close the browser window
driver.quit()
