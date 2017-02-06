from selenium import webdriver
import time

import os

class RunChromeTests(object):

    def test(self):

        driver_location = '/home/anna/bin/chromedriver'
        os.environ["webdriver.chrome.driver"] = driver_location
        driver = webdriver.Chrome(driver_location, service_args=["--verbose", "--log-path=chrome.log"])
        driver.get('http://www.google.com')
        time.sleep(5)
chr = RunChromeTests()
chr.test()