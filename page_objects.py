from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def open_page():
    # create webdriver page
    print("Open page")
    driver.get("https://www.geeksforgeeks.org/")
