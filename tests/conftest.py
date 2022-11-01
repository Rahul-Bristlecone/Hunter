import time

import pytest
import selenium
from selenium import webdriver

@pytest.fixture
def homepage():
    # edgebrowser = webdriver.Edge("E:\\Rahul_sharma\\Selenium_Testing\\venv\\selenium_testcases\\msedgedriver.exe")
    b =  selenium.webdriver.Chrome("E:\\Rahul_sharma\\Selenium_Testing\\chromedriver.exe")
    # open browser and navigate to homepage of URL
    # edgebrowser.implicitly_wait(5)
    b.implicitly_wait(15)
    b.maximize_window()
    time.sleep(10)
    # yield edgebrowser
    # Cleaning up the residue
    # edgebrowser.quit()
    # b.quit()