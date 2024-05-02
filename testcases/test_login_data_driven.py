import pytest
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from Page_Objects.Login_page import LoginPage 
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
from selenium import webdriver


@pytest.mark.usefixtures("init_driver")
class Test_002_DDT_Login:
    # base_url = f"https://admin-demo.nopcommerce.com/login"
    # username = "admin@yourstore.com"
    # password = "admin"
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    path = os.path.normpath("E:\Internship\SDET_selenium\Sotware_Testing_with_Pytest_POM_Selenium\TestData\LoginData.xlsx")

    def test_Login(self):
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        list_status = []
        for r in range(2,self.rows+1):
            self.username = ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path,'Sheet1',r,2)
            self.expected = ExcelUtils.readData(self.path,'Sheet1',r,3)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()

            actual_title = "Dashboard / nopCommerce administration"
            self.logger.info("******Verifying Login Test DDT 002******")
            if actual_title == self.driver.title:
                if self.expected == "Pass":
                    self.logger.info("******passed******")
                    self.lp.click_logout()
                    list_status.append("Pass")
                    assert True
                else:
                    self.logger.info("******Failed******")
                    self.lp.click_logout()
                    list_status.append("Fail")
                    assert True
            else:
                if self.expected == "Pass":
                    self.logger.info("******Failed******")
                    list_status.append("Fail")
                    assert True
                else:
                    self.logger.info("******Passed******")
                    list_status.append("Pass")
                    assert True
            if 'Fail' not in list_status:
                self.logger.info("logging passed")
                assert True
            else:
                self.logger.info("*****logging data test Failed*****")
                assert False
            
