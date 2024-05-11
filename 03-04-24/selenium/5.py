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

driver.find_element(By.XPATH, "//input[@class='search-box-text']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

# driver.find_element(By.XPATH, "input[@class='search-box-text' or  @name='q']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH, "//input[@name='q' or @id='small-searchterms']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")