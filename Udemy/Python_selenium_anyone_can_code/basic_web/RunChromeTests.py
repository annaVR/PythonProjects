from selenium import webdriver

import os

import time

class RunChromeTests(object):

    def test(self):
        driver_location = '/Users/anna/bin/chromedriver'
        os.environ['webdriver.chrome.driver'] = driver_location

        driver = webdriver.Chrome(driver_location)
        driver.get("http://www.google.com")
        time.sleep(5)

   
chr = RunChromeTests()
chr.test()
