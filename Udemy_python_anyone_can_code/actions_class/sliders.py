__author__ = 'anna'

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def slider():
    driver_location = '/Users/anna/bin/chromedriver'
    os.environ['webdriver.chrome.driver'] = driver_location
    driver = webdriver.Chrome(driver_location)

    driver.maximize_window()
    driver.get("https://jqueryui.com/slider/")
    driver.implicitly_wait(3)

    driver.switch_to.frame(0)
    slider = driver.find_element(By.XPATH, "//div[@id='slider']//span")
    time.sleep(2)
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider, 200, 0).perform()
    actions.drag_and_drop_by_offset()
    time.sleep(3)
    driver.quit()

slider()
