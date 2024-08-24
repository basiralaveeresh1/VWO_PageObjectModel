from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//input[@name='username' and @placeholder='Username']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "(//button[normalize-space()='Login'])"
    #dashboard_Admin_lin_ktext = "//span[text()='Admin']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()


    # def ClickDashboard(self):
    #     self.driver.find_element(By.LINK_TEXT,"dashboard_Admin_lin_ktext").click()


