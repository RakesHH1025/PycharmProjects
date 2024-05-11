from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.snapdeal.com")
driver.maximize_window()
time.sleep(2)

driver.get("https://www.amazon.com")
driver.maximize_window()
time.sleep(2)

driver.back()

time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(5)

driver.close()