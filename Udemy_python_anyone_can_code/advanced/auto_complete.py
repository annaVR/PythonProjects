__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
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
        sfo.click()
        time.sleep(2)
        driver.quit()

    def test_expedia(self):
        url = 'https://expedia.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("new")
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
        la_guardia = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='typeaheadDataPlain']//a[contains(@data-value,'LaGuardia')]")))
        la_guardia.click()
        time.sleep(2)
        driver.quit()

ff = AutoComplete()
#ff.test_southwest()
ff.test_expedia()



