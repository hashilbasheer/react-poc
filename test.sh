#!/bin/bash

# Install Selenium and ChromeDriver
pip install selenium
apt-get update
apt-get install -y chromium-browser
wget https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

# Run the test case
python my_selenium_test.py
