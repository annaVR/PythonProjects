__author__ = 'anna'

from selenium import webdriver

class BrowserInteractions(object):

    def test(self):
        driver = webdriver.Firefox()
        driver.get('https://letskodeit.teachable.com/p/practice')