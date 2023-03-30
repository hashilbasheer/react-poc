from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define the URL of the webpage you want to visit
url = "http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/"

# Define the path to the chromedriver executable
driver_path = "/usr/local/bin/chromedriver"

# Create a ChromeOptions object and set it to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')

# Create a new Chrome webdriver with the specified options
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Visit the webpage
driver.get(url)

# Get the title of the webpage
title = driver.title

# Print the title
print(title)

# Close the webdriver
driver.quit()
