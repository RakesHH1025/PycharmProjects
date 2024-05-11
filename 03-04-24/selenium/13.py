import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
# O=webdriver.ChromeOptions()
# O.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=S)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

dropdown=Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("India")

time.sleep(10)