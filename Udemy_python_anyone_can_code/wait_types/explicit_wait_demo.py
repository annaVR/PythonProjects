__author__ = 'anna'


from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time


class ExplictWaitDemo():

    def test(self):
        url = 'http://www.expedia.com'
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)


        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, 'flight-origin-hp-flight').send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, 'flight-destination-hp-flight').send_keys(Keys.RETURN)

        departure_field = driver.find_element(By.ID, "flight-departing-hp-flight")
        departure_field.click()

        departure_date = driver.find_element_by_xpath("//button[@data-day='26']")
        departure_date.click()

        time.sleep(3)
        return_field = driver.find_element(By.ID, "flight-returning-hp-flight")
        return_field.click()
        return_date = driver.find_element_by_xpath("//button[@data-day='28']")
        return_date.click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//button[@class="btn-primary btn-action gcw-submit"]').click()

        wait = WebDriverWait(driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                              ElementNotVisibleException,
                                                                              ElementNotSelectableException])
        nonstop_filter = wait.until(EC.element_to_be_clickable((By.ID, 'stopFilter_stops-0')))
        one_stop_filter = wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-1")))
        united_filter = wait.until(EC.element_to_be_clickable((By.ID, "airlineRowContainer_UA")))

        time.sleep(2)
        nonstop_filter.click()
        one_stop_filter.click()
        united_filter.click()

        time.sleep(2)
        driver.quit()

ch = ExplictWaitDemo()
ch.test()

