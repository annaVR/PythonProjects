__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def switch_to_javascript_alert():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://letskodeit.teachable.com/p/practice")
    driver.implicitly_wait(3)
    driver.find_element(By.ID, 'name').send_keys('Anna')
    driver.find_element(By.ID, 'alertbtn').click()
    time.sleep(3)

    alert1 = driver.switch_to.alert
    alert1.accept()
    time.sleep(2)
    driver.find_element(By.ID, 'name').send_keys('Anna')

    driver.find_element(By.ID, 'confirmbtn').click()
    time.sleep(2)
    alert2 = driver.switch_to.alert
    alert2.dismiss()
    time.sleep(2)
    driver.quit()


    alert3 = driver.switch_to.alert
    alert3.accept()
    alert3.dismiss()

    
switch_to_javascript_alert()