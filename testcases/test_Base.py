import pytest
import time
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from Page_Objects.Login_page import LoginPage
from Page_Objects.AddCustomerPage import AddCustomer
from Page_Objects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # def __init__(self,driver):
    #     self.driver=driver