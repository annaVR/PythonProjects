__author__ = 'anna'

from selenium import webdriver
import time

def execute_java_script():
    driver = webdriver.Chrome()
    driver.execute_script('window.location = "https://letskodeit.teachable.com/p/practice";')
    driver.implicitly_wait(3)

    #time.sleep added because driver.implicitly_wait is not working if we execute script
    time.sleep(3)
    height = driver.execute_script('return window.innerHeight;')
    width = driver.execute_script('return window.innerWidth;')
    print(height, width)
    driver.maximize_window()

    element = driver.execute_script('return document.getElementById("displayed-text");')
    element.send_keys('Done')
    time.sleep(3)
    height = driver.execute_script('return window.innerHeight;')
    width = driver.execute_script('return window.innerWidth;')
    print(height, width)
    driver.quit()
execute_java_script()
