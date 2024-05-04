import pytest
import time
from test_Base import BaseTest
import test_Base

class Test_SearchCustomerByEmail_004(BaseTest):

    # def __init__(self,driver):
    #     super().__init__(driver)
    testbase = BaseTest()
    @pytest.mark.regression
    def test_SearchCustomerByEmail(self):
        # self.testbase = BaseTest()
        
        self.testbase.logger.info("*****search customer by email 004 started******")
        self.driver.get(self.testbase.baseURL)
        self.driver.maximize_window()

        self.lp = test_Base.LoginPage(self.driver)
        self.lp.set_username(self.testbase.username)
        self.lp.set_password(self.testbase.password)
        self.lp.click_login()
        self.testbase.logger.info("******Login Successfull*******")
        assert "Dashboard / nopCommerce administration" == self.driver.title

        self.testbase.logger.info("******* Starting Search Customer By Email **********")
        self.addcust = test_Base.AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.testbase.logger.info("****** customer menu reached *******")

        self.searchcus = test_Base.SearchCustomer(self.driver)
        self.searchcus.setEmail("victoria_victoria@nopCommerce.com")

        self.searchcus.clickSearch()

        search_status = self.searchcus.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == search_status
        self.testbase.logger.info("*****search customer by email finished*****")