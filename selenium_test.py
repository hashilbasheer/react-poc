from selenium import webdriver

# Define the URL of the webpage you want to visit
url = "http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/"

# Define the path to the chromedriver executable
driver_path = "/usr/local/bin/chromedriver"


# Create a new Chrome webdriver
driver = webdriver.Chrome(executable_path=driver_path)

# Visit the webpage
driver.get(url)

# Get the title of the webpage
title = driver.title

# Print the title
print(title)

# Close the webdriver
driver.quit()




