from selenium import webdriver

# Set up the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Navigate to the URL of the React application
url = "http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/"
driver.get(url)

# Perform some basic health checks
assert "React App" in driver.title
assert "Welcome to React" in driver.page_source

# Close the browser window
driver.quit()
