from selenium import webdriver

import os

import time

class RunSafariTests(object):

    def test(self):
        server_location = '/Users/anna/bin/selenium-server-standalone-2.53.1.jar'
        os.environ['SELENIUM_SERVER_JAR'] = server_location

        driver = webdriver.Safari()
        driver.get("http://www.google.com")
        time.sleep(10)

sf = RunSafariTests()
sf.test()
