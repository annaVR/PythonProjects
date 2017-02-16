__author__ = 'anna'


import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from wrappers import Wrappers
import time

sys.path.insert(0, 'users/anna/PycharmProjects/PythonProjects/Udemy_python_anyone_can_code/tools)')

class ElementPresentCheck():

    def test(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        wrapper = Wrappers(driver)
        driver.implicitly_wait(4)
        print(wrapper.is_element_present('Css', 'kdfn'))
        print(wrapper.is_element_present('css', '#openwindow'))
        print(wrapper.is_element_present_list_method(By.CSS_SELECTOR, 'kdfn'))
        print(wrapper.is_element_present_list_method(By.CSS_SELECTOR, '#openwindow'))
        driver.quit()

check = ElementPresentCheck()
check.test()
