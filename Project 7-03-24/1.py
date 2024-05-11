from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class Opencart:
    def __init__(self,driver):
        self.driver = driver

    serv_obj = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=serv_obj)

    url="https://www.opencart.com/index.php?route=account/register"
    txt_firstname = "firstname"
    txt_lastname = "lastname"
    txt_email = "email"
    txt_password = "password"
    chk_policy_name = "agree"
    btn_cont_xpath = "//button[@class='btn btn-primary']"
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def register(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "self.txt_firstname").send_keys('Rakesh')
        self.driver.find_element(By.NAME, "self.txt_lastname").send_keys('Bogaa')
        self.driver.find_element(By.NAME, "self.txt_email").send_keys("rakesh.rakz001@gmail.com")
        button=self.driver.find_element(By.XPATH, "self.chk_policy_name")
        button.click()
        self.driver.find_element(By.XPATH, "self.btn_cont_xpath").click()

obj=Opencart
obj.register()