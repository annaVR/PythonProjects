__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def test(self):

        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        driver.implicitly_wait(4)

        radio_button_list = driver.find_elements(By.XPATH,
                                                 '//input[contains(@type, "radio") and contains(@name, "cars")]')
        for element in radio_button_list:
            if not element.is_selected():
                element.click()
                time.sleep(3)

        check_box_list = driver.find_elements(By.XPATH,
                                              '//input[contains(@type, "checkbox") and contains(@name, "cars")]')
        for element in check_box_list:
            if not element.is_selected():
                element.click()
                time.sleep(3)
            if element.is_selected():
                element.click()
                time.sleep(3)
        driver.quit()

ff = WorkingWithElementsList()
ff.test()
