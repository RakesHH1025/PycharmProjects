import pytest
from Pageobjects.HomePage import HomePage
from Pageobjects.AccountRegistrationpage import AccountRegistrationpage
from utilities import randomstring
import os
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Accountreg:
    baseurl=Readconfig.getapplicationurl()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_account_reg(self,setup):
        self.driver=setup
        self.logger.info("**test_001_accountstarted**")
        self.driver.get(self.baseurl)
        self.logger.info("Launchapplication")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Proving customer details for registration")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed..")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.logger.error("Account registration is failed.")
            self.driver.close()
            assert False
        self.logger.info("**** test_001_AccountRegistration finished *** ")
