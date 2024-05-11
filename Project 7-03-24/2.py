from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Opencart:
    def __init__(self, driver_path):
        self.serv_obj = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=self.serv_obj)
        self.url = "https://www.opencart.com/index.php?route=account/register"
        self.txt_firstname = "firstname"
        self.txt_lastname = "lastname"
        self.txt_email = "email"
        self.txt_password = "password"
        self.chk_policy_name = "agree"
        self.btn_cont_xpath = "//button[@class='btn btn-primary']"
        self.text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def register(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, self.txt_firstname).send_keys('Rakesh')
        self.driver.find_element(By.NAME, self.txt_lastname).send_keys('Bogaa')
        self.driver.find_element(By.NAME, self.txt_email).send_keys("rakesh.rakz001@gmail.com")
        button = self.driver.find_element(By.XPATH, self.chk_policy_name)
        button.click()
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

# Instantiate Opencart object
opencart_obj = Opencart("D:\Drivers\chromedriver-win64\chromedriver.exe")
opencart_obj.register()
