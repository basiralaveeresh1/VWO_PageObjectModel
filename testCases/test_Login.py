import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_homePageTitle(self,setup):

        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
        else:
            assert False
        self.driver.close()

    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(5)
        # Creating the Class Object here (class Name -- LoginPage, its importing from other packages)
        self.LP = LoginPage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.ClickLogin()
        act_Title = self.driver.title
        if act_Title == "OrangeHRM":
            assert True
        else:
            assert False
        time.sleep(3)



