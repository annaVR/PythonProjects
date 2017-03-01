__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test_southwest(self):

        url = 'https://southwest.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        driver.implicitly_wait(5)

        departure = driver.find_element(By.ID, "air-city-departure").send_keys('SFO')
        time.sleep(3)
        suggestions_list = driver.find_elements(By.XPATH, "//ul[@id='air-city-departure-menu']//li[@role='option']")
        print(len(suggestions_list))
        sfo = driver.find_element(By.XPATH, "//ul[@id='air-city-departure-menu']//li[contains(text(), 'San F')]")
        time.sleep(2)
        sfo.click ()
        time.sleep(2)
        driver.quit()
ff = AutoComplete()
ff.test_southwest()



