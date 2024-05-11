from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
o=webdriver.ChromeOptions()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o, service=s)


driver.get("https://www.facebook.com/")
driver.maximize_window()

#TAG ID
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("123456899")
# driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("987456321")

#TAG CLASS
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("123456899")
# driver.find_element(By.CSS_SELECTOR, ".").send_keys("987456321")

# TAG ATTRIBUTE
# driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("123456899")
# driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys("987456321")

time.sleep(5)
# TAG CLASS ATTRIBUTE
driver.find_element(By.CSS_SELECTOR, "input.inputtext[name='email']").send_keys("123456899")
driver.find_element(By.CSS_SELECTOR, ".inputtext[name='pass']").send_keys("123456899")

driver.close()