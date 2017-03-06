__author__ = 'anna'

from selenium import webdriver
import time
import datetime

def ff_setup(url):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(4)
    return driver

def take_screenshot(driver):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d:%H:%M:%S')
    destination = '/home/anna/Documents/{}.png'.format(st)
    driver.save_screenshot(destination)

