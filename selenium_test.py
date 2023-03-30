from selenium import webdriver
import os

try:
    # Define the URL you want to test
    URL = "http://volvosalescockpit.6ed500daefb04e85a911.eastus.aksapp.io/"

    # Define the path to the chromedriver executable
    DRIVER_PATH = "/usr/local/bin/chromedriver"

    # Set the Github Actions secret token as an environment variable
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

    # Create a new Chrome webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Run Chrome in headless mode
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    # Visit the URL
    driver.get(URL)

    # Find the page title element and assert that it contains the expected text
    assert "Example Domain" in driver.title

    # Print a success message
    print("Test passed!")

    # Set the Github Actions status to "success"
    os.system(f'curl -H "Authorization: token {GITHUB_TOKEN}" \
                  --request POST \
                  --data \'{{"state": "success"}}\' \
                  https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/statuses/{os.environ["GITHUB_SHA"]}')

except AssertionError:
    # If the assertion fails, print an error message and set the Github Actions status to "failure"
    print("Error: page title does not contain expected text")
    os.system(f'curl -H "Authorization: token {GITHUB_TOKEN}" \
                  --request POST \
                  --data \'{{"state": "failure", "description": "Page title does not contain expected text"}}\' \
                  https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/statuses/{os.environ["GITHUB_SHA"]}')

except Exception as e:
    # Print any exceptions that occur during the script run and set the Github Actions status to "failure"
    print(f"Error: {e}")
    os.system(f'curl -H "Authorization: token {GITHUB_TOKEN}" \
                  --request POST \
                  --data \'{{"state": "failure", "description": "Error occurred during test run"}}\' \
                  https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/statuses/{os.environ["GITHUB_SHA"]}')
