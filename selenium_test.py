from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request

# Define the URL of the webpage you want to visit
url = "http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/"

# Define the path to the chromedriver executable
driver_path = "/usr/local/bin/chromedriver"

# Set up the Chrome options for running in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Create a new Chrome webdriver with the headless option
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Visit the webpage
driver.get(url)

# Get the current URL after any redirects
current_url = driver.current_url

# Get the status code of the current URL
status_code = urllib.request.urlopen(current_url).getcode()

# Print the status code
print(status_code)

# Close the webdriver
driver.quit()
