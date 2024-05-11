from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

checkbox=driver.find_element(By.XPATH, "//input[@id='sunday']")
checkbox.click()
time.sleep(3)

checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for i in checkboxes:
    i.click()