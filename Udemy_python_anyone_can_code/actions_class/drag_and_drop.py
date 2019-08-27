__author__ = 'anna'

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def drag_and_drop():

    driver = webdriver.Chrome()

    #driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    driver.implicitly_wait(3)

    driver.switch_to.frame(0)
    draggable = driver.find_element(By.ID, 'draggable')
    droppable = driver.find_element(By.ID, 'droppable')
    actions = ActionChains(driver)
    time.sleep(2)
    #one way
    #actions.drag_and_drop(draggable, droppable).perform()

    #the other way
    actions.click_and_hold(draggable).move_to_element(droppable).release(droppable).perform()

    time.sleep(2)
    driver.quit()
drag_and_drop()
