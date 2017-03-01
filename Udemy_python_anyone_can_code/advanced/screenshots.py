__author__ = 'anna'

import sys
sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/Udemy_python_anyone_can_code/tools')

from selenium.webdriver.common.by import By
import time
from driver_setup import ff_setup

def screenshot(url):
    driver = ff_setup(url)




screenshot('https://letskodeit.teachable.com/p/practice')