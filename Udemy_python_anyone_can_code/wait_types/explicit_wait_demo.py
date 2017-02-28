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

        driver.find_element(By.ID, "tab-flight-tab").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, 'flight-origin-hp-flight').send_keys(Keys.RETURN)
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, 'flight-destination-hp-flight').send_keys(Keys.RETURN)

        driver.find_element(By.ID, "flight-departing").click()
        driver.find_element(By.XPATH,
                            "//caption[contains(text(),'FEB 2017')]/parent::table//button[contains(text(), '25')]").click()

        time.sleep(3)
        return_date = driver.find_element(By.ID, "flight-returning").click()
        driver.find_element(By.XPATH,
                            "//caption[contains(text(),'FEB 2017')]/parent::table//button[contains(text(), '27')]").click()

        time.sleep(3)
        #another test for the car tab
        # driver.find_element(By.ID, "tab-car-tab").click()
        # driver.find_element(By.ID, "car-pickup").send_keys('San Francisco\n')
        # time.sleep(2)
        # driver.find_element(By.ID, 'car-dropoff').send_keys('Los Angeles\n')
        # time.sleep(2)
        #
        # pickup_date = driver.find_element(By.ID, "car-pickup-date")
        # pickup_date.clear()
        # pickup_date.send_keys('02/25/2017\n')
        # time.sleep(2)
        # pickup_time = driver.find_element(By.ID, "car-pickup-time")
        # time.sleep(2)
        #
        # pickup_time_options = Select(pickup_time)
        # pickup_time_options.select_by_value('900AM')
        # driver.find_element(By.ID, "car-dropoff-date").send_keys('02/27/2017\n')
        # dropoff_time = driver.find_element(By.ID, "car-dropoff-time")
        # dropoff_time_options = Select(dropoff_time)
        # dropoff_time_options.select_by_value("600PM")
        # time.sleep(4)
        driver.find_element(By.ID, "search-button").click()

        wait = WebDriverWait(driver, 60, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, 'stopFilter_stops-0')))
        time.sleep(2)
        element.click()
        time.sleep(2)
        print('Just some exercise in XPath:')
        month_calendar = driver.find_element(By.XPath, "//caption[contains(text(), 'FEB 2017')]/parent::table")
        calendar_days = month_calendar.find_elements(By.XPATH, "//button[not(contains(@class, 'disabled'))]")
        print('The number or days: {}'.format(len(calendar_days)))
        time.sleep(2)
        driver.quit()

ff = ExplictWaitDemo()
ff.test()

