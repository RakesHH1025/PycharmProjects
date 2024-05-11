from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

S=Service('D:\Drivers\chromedriver-win64\chromedriver.exe')
o=webdriver.ChromeOptions()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o, service=S)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# driver.find_element(By.CLASS_NAME, "button-1").click()
# driver.find_element(By.TAG_NAME, "")

# driver.find_element(By.LINK_TEXT, "Register")

driver.find_element(By.PARTIAL_LINK_TEXT, "Reg")