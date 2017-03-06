__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrolling():
    driver = webdriver.Firefox()
    driver.execute_script('window.location = "https://letskodeit.teachable.com/p/practice";')

    time.sleep(4)
    # driver.maximize_window()
    driver.implicitly_wait(3)

    #using javascipt
    driver.execute_script('window.scrollBy(0, 1000);')
    time.sleep(5)
    driver.execute_script('window.scrollBy(0, -1000);')
    time.sleep(5)
    element = driver.find_element(By.ID, 'mousehover')
    driver.execute_script('arguments[0].scrollIntoView(true);', element)
    time.sleep(5)
    # heather will come up, so the element will be in our view, but behind the heather.
    # so, we scroll down a little bit

    driver.execute_script('window.scrollBy(0, -150);')
    time.sleep(5)
    driver.execute_script('window.scrollBy(0, -1500);')
    time.sleep(5)

    #using swd
    location = element.location_once_scrolled_into_view # return a location in pixels from the left corner of the screen
    print(location)
    time.sleep(5)
    # heather will come up, so the element will be in our view, but behind the heather.
    # so, we scroll down a little bit
    driver.execute_script('window.scrollBy(0, -150);')
    time.sleep(5)
    driver.quit()

scrolling()

