from selenium import webdriver
import time

import os

class RunChromeTests(object):

    def test(self):

        #driver_location = '/Users/annaromanovskaia/bin/chromedriver'
        #os.environ["webdriver.chrome.driver"] = driver_location
        #Commented out chromedriver location setup to os.environ because I did set it up in .bash_profile
        driver = webdriver.Chrome(service_args=["--verbose", "--log-path=chrome.log"])
        #this is argument to webdriver.Chrome() if I did not setup it in .bash_profile driver_location
        driver.get('http://www.google.com')
        time.sleep(5)
chr = RunChromeTests()
chr.test()