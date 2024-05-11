import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

o=webdriver.ChromeOptions()
S=Service()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o, service=S)

driver.get("https://www.limeroad.com/auth/login")
driver.maximize_window()

# driver.find_element(By.XPATH, "//div[contains(text(),'Profile')]").click()
driver.find_element(By.XPATH, "//input[@id='emph']").send_keys("7075689770")
driver.find_element(By.XPATH, "//input[@value='NEXT']").click()
time.sleep(10)
