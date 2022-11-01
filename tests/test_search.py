from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.bing_search_page import bing_searchpage
from pages.bing_result import bing_resultpage
def test_bing(homepage):
    search_page = bing_searchpage(homepage)
    result_page = bing_resultpage(homepage)
    # Comments for Test Cases - Testing (Not development)
    # edgeBrowser = webdriver.Edge("E:\\Rahul_sharma\\Selenium_Testing\\venv\\selenium_testcases\\msedgedriver.exe")
    # open browser and navigate to URL
    # edgeBrowser.maximize_window()

    search_page.load()
    search_page.search("panda")
    assert "panda" in result_page.title()
    # Given : The browser is opened
    # When : The URL is entered
    # edgeBrowser.get('https://www.flipkart.com')
    # Then : URL should open (Server should sent a response)
    # When : The user click on the "cross"
    # edgeBrowser.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()
    # Then : The pop-up window should get closed &
    # Then : Home page should appear
    # edgeBrowser.save_screenshot("E:\\Rahul_sharma\\Selenium_Testing\\venv\\selenium_testcases\\Screenshots\\login.png")
    # print("Screenshot taken")
    # edgeBrowser.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()
    print("success")