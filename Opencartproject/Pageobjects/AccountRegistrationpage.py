from selenium.webdriver.common.by import By

class AccountRegistrationpage:
    txt_firstname="firstname"
    txt_lastname="lastname"
    txt_email="email"
    txt_password="password"
    chk_policy_name="agree"
    btn_cont_xpath="//button[@class='btn btn-primary']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver=driver

    def setfirstname(self,fname):
        self.driver.find_element(By.NAME, self.txt_firstname).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME, self.txt_lastname).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME, self.txt_email).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password).send_keys(pwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def getconfirmationmsg(self):
        try:
            return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None



