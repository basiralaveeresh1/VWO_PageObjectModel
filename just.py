import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
#driver.find_element(By.CSS_SELECTOR,"[placeholder='Username']")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,"(//button[normalize-space()='Login'])").click()
time.sleep(4)