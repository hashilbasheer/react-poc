from selenium import webdriver

# Initialize Chrome webdriver
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

# Navigate to URL
driver.get('http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io')

# Verify that the page title is correct
assert 'React App1' in driver.title

# Close the browser
driver.quit()
