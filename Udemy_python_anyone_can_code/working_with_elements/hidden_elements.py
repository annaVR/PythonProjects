__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class HiddenElements(object):

    def test_letskodeit(self):

        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        element = driver.find_element(By.ID, "displayed-text")
        print(element.is_displayed())
        time.sleep(3)
        driver.find_element(By.ID, 'hide-textbox').click()
        time.sleep(3)
        print(element.is_displayed())
        driver.find_element(By.ID, 'show-textbox').click()
        time.sleep(3)
        print(element.is_displayed())
        driver.quit()

    def test_expedia(self):
        url = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        driver.find_element(By.ID, "tab-flight-tab").click()
        driver.implicitly_wait(3)

        element = driver.find_element(By.ID, "flight-children")
        for i in range(2):

            try:
                drop_down = driver.find_element(By.ID, "flight-age-select-1")
                options_list = driver.find_elements(By.XPATH, '//select[@id="flight-age-select-1"]/option')
                length_options = len(options_list)
                options = Select(drop_down)
                options.select_by_value('6')
                print('Success!')

            except:
                print('The element does not exist on the DOM')
                flight_tab_options = Select(element)
                flight_tab_options.select_by_value('1')
                time.sleep(2)
        driver.quit()

ff = HiddenElements()
# ff.test_letskodeit()
ff.test_expedia()
