__author__ = 'anna'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time


class ExplictWaitDemo():

    def test(self):
        url = 'http://www.expedia.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, 'flight-origin-hp-flight').send_keys(Keys.RETURN)
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, 'flight-destination-hp-flight').send_keys(Keys.RETURN)

        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        print('Just some exercise in XPath:')
        month_calendar = driver.find_elements(By.XPATH, "//caption[contains(text(), 'Mar 2017')]/parent::table//button")

        print('The number or days: {}'.format(len(month_calendar)))
        for element in month_calendar:
            print(element.text)
        time.sleep(2)
        driver.quit()

ff = ExplictWaitDemo()
ff.test()
