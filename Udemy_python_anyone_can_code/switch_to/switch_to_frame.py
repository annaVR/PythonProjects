__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def switch_to_frame():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://letskodeit.teachable.com/p/practice")
    driver.implicitly_wait(3)
    driver.execute_script('window.scrollBy(0, 2000);')

    driver.switch_to.frame('courses-iframe')
    time.sleep(2)

    driver.find_element(By.ID, 'search-courses').send_keys('Linux')
    time.sleep(2)
    driver.find_element(By.ID, "search-course-button").click()
    time.sleep(3)

    driver.switch_to.default_content()
    driver.execute_script('window.scrollBy(0, -2000)')
    time.sleep(2)
    driver.find_element(By.ID, 'name').send_keys('Test completed')
    time.sleep(2)
    driver.quit()

switch_to_frame()