from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O,service=S)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "downloads").click()

links=driver.find_elements(By.XPATH, "//a")
print(len(links))

for i in links:
    print(i.text)
