__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class HiddenElements(object):

    def test_letskodeit(self):

        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
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
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        driver.find_element(By.XPATH, "//span[contains(text(),'Flights')]").click()

        driver.implicitly_wait(3)
        buttons = driver.find_elements(By.XPATH, "//span[text()='Add Adult']//parent::button")
        print("Button state: {}".format(buttons[0].is_displayed()))
        try:
            travelers = driver.find_element(By.XPATH, "//div[@id='traveler-selector-hp-flight']//ul[@class='menu-bar-inner']/li/button[@type='button']")
            travelers.click()
            time.sleep(3)
        except:
            print("Failed")
        print("Button state: {}".format(buttons[0].is_displayed()))
        buttons[0].click()
        time.sleep(4)
        driver.quit()

ff = HiddenElements()
ff.test_letskodeit()
ff.test_expedia()

