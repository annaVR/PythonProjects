__author__ = 'anna'


import sys
sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/Udemy_python_anyone_can_code/tools')

from selenium import webdriver
from custom_helpers import ff_setup
from custom_helpers import take_screenshot

url = 'https://letskodeit.teachable.com/p/practice'
driver = ff_setup(url)
take_screenshot(driver)
driver.quit()