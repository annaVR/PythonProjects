__author__ = 'anna'

from selenium import webdriver

def ff_sep_up(url):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(4)
    return driver

