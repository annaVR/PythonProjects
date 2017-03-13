__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def switch_to_window():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://letskodeit.teachable.com/p/practice")
    driver.implicitly_wait(3)

    parent_handle = driver.current_window_handle
    print(parent_handle)

    driver.find_element(By.ID, 'openwindow').click()
    time.sleep(2)

    handles = driver.window_handles
    print(handles)
    for handle in handles:
        print(handle)
        if handle != parent_handle:
            driver.switch_to.window(handle)
            print('switch to: {}'.format(handle))
            search_box = driver.find_element(By.ID, 'search-courses')
            search_box.send_keys('java')
            time.sleep(3)
            driver.close()
    driver.switch_to.window(parent_handle)
    driver.find_element(By.ID, 'name').send_keys('Success')
    time.sleep(3)
    driver.quit()

def switch_to_window_random():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://letskodeit.teachable.com/p/practice")
    driver.implicitly_wait(3)

    parent_handle = driver.current_window_handle
    print(parent_handle)

    courses = ['Python_tutorial', 'Java', 'JavaScript', 'Linux']

    for _ in range(3):
        driver.find_element(By.ID, 'openwindow').click()
        handles = driver.window_handles
        for handle in handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                print('Switched to {}'.format(handle))
                course = random.choice(courses)
                driver.find_element(By.ID, 'search-courses').send_keys(course)
                time.sleep(3)
                driver.find_element(By.ID, "search-course-button").click()
                time.sleep(3)
                driver.close()
                driver.switch_to.window(parent_handle)
                driver.find_element(By.ID, 'name').send_keys('Done')
                time.sleep(3)

    time.sleep(2)

    handles = driver.window_handles
    print(handles)

    driver.quit()


# switch_to_window()
switch_to_window_random()