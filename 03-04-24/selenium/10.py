from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.implicitly_wait(10)

driver.get('https://www.google.com/')
driver.maximize_window()

search=driver.find_element(By.NAME, "q")
search.send_keys("Selenium")
search.submit()

driver.find_element(By.XPATH, "//h3[contains(text(),'Selenium')]").click()
time.sleep(3)