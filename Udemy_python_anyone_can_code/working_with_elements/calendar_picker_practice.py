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
        driver = webdriver.Chrome()
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
        valid_dates_current_month = driver.find_elements_by_xpath("//div[@class='datepicker-cal-month'][1"
                                                                  "]//button[@class='datepicker-cal-date']")
        print('The number or days: {}'.format(len(valid_dates_current_month)))
        for element in valid_dates_current_month:
            print(element.get_attribute("data-day"))
        time.sleep(2)
        #driver.quit()

ch = ExplictWaitDemo()
ch.test()
