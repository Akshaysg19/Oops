from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.ChromeOptions()
driver.add_argument('--headless')
def open_page():
    # create webdriver page
    print("Open page")
    driver = webdriver.Chrome()
    driver.get("https://www.geeksforgeeks.org/")
