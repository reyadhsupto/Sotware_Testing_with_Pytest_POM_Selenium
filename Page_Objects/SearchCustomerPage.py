import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class SearchCustomer():
    # Add customer Page
    txtEmail_id = (By.ID, 'SearchEmail')
    txtFirstName_id= (By.ID, 'SearchFirstName')
    txtLastName_id= (By.ID, 'SearchLastName')
    btnSearch_id= (By.XPATH, "//button[@id='search-customers']")
    # tblSearchResults_xpath="//table[@role='grid']"
    table_xpath= (By.XPATH, "//table[@id='customers-grid']")
    tableRows_xpath= (By.XPATH, "//table[@id='customers-grid']/tbody/tr")
    tableColumns_xpath= (By.XPATH, "//table[@id='customers-grid']/tbody/tr/td")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email:str):
        element = self.driver.find_element(*self.txtEmail_id)
        element.clear()
        element.send_keys(email)

    def setFirstName(self,fname):
        element = self.driver.find_element(*self.txtFirstName_id)
        element.clear()
        element.send_keys(fname)

    def setLastName(self,lname):
        element = self.driver.find_element(*self.txtLastName_id)
        element.clear()
        element.send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(*self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(*self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(*self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(*self.table_xpath)
          emailid=table.find_element(By.XPATH, "./tbody/tr["+str(r)+"]/td[2]").get_attribute("textContent")
          if emailid == email:
              return True
        return False

    def searchCustomerByName(self,Name):
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(*self.table_xpath)
          name=table.find_element(By.XPATH, "./tbody/tr["+str(r)+"]/td[3]").get_attribute("textContent")
          if name == Name:
              return True
        return False

