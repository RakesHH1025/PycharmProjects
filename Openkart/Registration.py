from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service=Service()
o=webdriver.ChromeOptions()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o, service=service)

driver.implicitly_wait(10)
driver.get("https://demo.opencart.com")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[contains(.,'My Account')]").click()
driver.find_element(By.XPATH, "//a[.='Register']").click()
driver.find_element(By.NAME, "firstname").send_keys("Pavan")
driver.find_element(By.NAME, "firstname").send_keys("Pavan")
driver.find_element(By.NAME, "firstname").send_keys("Pavan")
driver.find_element(By.NAME, "firstname").send_keys("Pavan")
