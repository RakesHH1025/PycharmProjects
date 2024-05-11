import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
inputbox=driver.find_element(By.NAME, "Email")
inputbox.clear()
inputbox.send_keys("admin@yourstore.com")
pswd=driver.find_element(By.ID, "Password")
pswd.clear()
pswd.send_keys("admin")
button=driver.find_element(By.CLASS_NAME, "button-1 ")
button.click()
time.sleep(5)

exp_title="Admin area demo"
act_title=driver.title

if act_title==exp_title:
    print("Test case passed")
else:
    print("Test case failed")

time.sleep(5)
driver.close()
