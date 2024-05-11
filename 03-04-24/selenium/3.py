from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
o=webdriver.ChromeOptions()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o, service=s)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

sliders=driver.find_elements(By.CLASS_NAME, "nivo-main-image")
print(len(sliders))

links=driver.find_elements(By.TAG_NAME, "a")
print(len(links))


driver.close()