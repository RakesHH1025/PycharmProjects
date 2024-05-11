from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

print(driver.title)
print(driver.page_source)
print(driver.current_url)