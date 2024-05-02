import pytest
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from Page_Objects.Login_page import LoginPage 
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver


@pytest.mark.usefixtures("init_driver")
class Test_001_Login:
    # base_url = f"https://admin-demo.nopcommerce.com/login"
    # username = "admin@yourstore.com"
    # password = "admin"
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homepage_Title(self):
        self.logger.info("******Test_001 Login******")
        self.driver.get(self.base_url)
        actual_title = "Your store. Login"
        self.logger.info("******Verifying Login Page Title******")
        assert self.driver.title == actual_title , f"Error Login page title not accurate"

    def test_Login(self):
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title = "Dashboard / nopCommerce administration"
        self.logger.info("******Verifying Login Test******")
        assert self.driver.title == actual_title , f"ERROR, Admin can't log in"