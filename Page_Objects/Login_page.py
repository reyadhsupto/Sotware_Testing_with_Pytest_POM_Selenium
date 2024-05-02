import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage:
    """class for login page"""
    textbox_username_id = (By.ID, "Email")
    textbox_password_id = (By.ID, "Password")
    button_loginbutton = (By.XPATH, "//button[contains(text(),'Log in')]")
    link_logout = (By.LINK_TEXT, "Logout")

    def __init__(self,driver):
        self.driver = driver
    
    def set_username(self,username):
        self.driver.find_element(*self.textbox_username_id).clear()
        self.driver.find_element(*self.textbox_username_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(*self.textbox_password_id).clear()
        self.driver.find_element(*self.textbox_password_id).send_keys(password) 

    def click_login(self):
        self.driver.find_element(*self.button_loginbutton).click()

    def click_logout(self):
        self.driver.find_element(*self.link_logout).click()