import subprocess
from selenium import webdriver

# Define the URL of the webpage you want to visit
url = "http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/"

# Define the path to the chromedriver executable
driver_path = "/usr/local/bin/chromedriver"

# Install the requests module using pip
subprocess.check_call(["pip", "install", "requests"])

# Create a new Chrome webdriver
driver = webdriver.Chrome(executable_path=driver_path)

# Visit the webpage
driver.get(url)

# Get the current URL after any redirects
current_url = driver.current_url

# Get the status code of the current URL
status_code = requests.get(current_url).status_code

# Print the status code
print(status_code)

# Close the webdriver
driver.quit()
