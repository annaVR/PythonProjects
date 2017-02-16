__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Practice(object):

    def airbnb_test(self):

        url = 'http://airbnb.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        where = driver.find_element(By.ID, "search-location")
        where.send_keys('Paris')
        time.sleep(2)

        check_in = driver.find_element(By.ID, "startDate")
        check_in.send_keys('2/19/2017')
        time.sleep(2)

        check_out = driver.find_element(By.ID, "endDate")
        check_out.send_keys('2/25/2017')
        time.sleep(2)

        button = driver.find_element(By.CSS_SELECTOR, ".GuestPickerTrigger__button")
        button.click()
        time.sleep(2)
        driver.implicitly_wait(4)

        increment_adults_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increment number of adults"]')
        for iteration in range(2):
            increment_adults_button.click()
            time.sleep(2)
        search_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-large.btn-block')
        search_button.click()
        time.sleep(10)

        driver.quit()

ff = Practice()
ff.airbnb_test()


