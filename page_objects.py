from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.ChromeOptions()
driver.add_argument('--headless')
driver = webdriver.Chrome()
def open_page():
    # create webdriver page
    print("Open page")
    driver.get("https://www.geeksforgeeks.org/")
    # get element
    element = driver.find_element(By.XPATH,"//div[@class='ant-row ant-row-center gfg_home_page_search_heading']")
    # close current window
    print(element.text)
    driver.close()

