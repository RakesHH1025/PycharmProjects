from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchDriverException,NoSuchElementException,NoSuchAttributeException

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=S)

# mywait=WebDriverWait(driver,10)
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchAttributeException,
                     NoSuchElementException,
                     NoSuchElementException])

driver.get("https://www.google.com/")
driver.maximize_window()
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()

search_link=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search_link.click()

driver.quit()