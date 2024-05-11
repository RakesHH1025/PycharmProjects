from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
o=webdriver.ChromeOptions()
o.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=o, service=S)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

searchbox=driver.find_element(By.ID, "small-searchterms")
searchbox.click()
print(searchbox.is_displayed())
print(searchbox.is_enabled())
print(searchbox.is_selected())