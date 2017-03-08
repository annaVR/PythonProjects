__author__ = 'anna'

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def mouse_hovering():
    driver_location = '/Users/anna/bin/chromedriver'
    os.environ['webdriver.chrome.driver'] = driver_location
    driver = webdriver.Chrome(driver_location)

    driver.maximize_window()
    driver.get("https://letskodeit.teachable.com/p/practice")
    driver.implicitly_wait(3)

    driver.execute_script('window.scrollBy(0, 800);')
    time.sleep(2)
    mouse_hover = driver.find_element(By.ID, 'mousehover')
    go_to_the_top_locator = "//div[@class='mouse-hover-content']//a[text()='Top']"

    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, go_to_the_top_locator).click()
    time.sleep(3)
    print('Success')

    time.sleep(2)
    driver.quit()
mouse_hovering()
