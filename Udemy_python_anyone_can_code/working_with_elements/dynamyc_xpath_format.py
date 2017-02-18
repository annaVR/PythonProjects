__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

class DynamicXPathFormat():

    def test(self):

        url = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        #login
        driver.find_element(By.LINK_TEXT, 'Login').click()
        driver.find_element(By.ID, 'user_email').send_keys('test@email.com')
        driver.find_element(By.ID, 'user_password').send_keys('abcabc')
        driver.find_element(By.NAME, 'commit').click()

        #select random course from the list and open its link
        courses_list = driver.find_elements(By.CSS_SELECTOR, '.course-listing-title')
        random_course = random.choice(courses_list)
        title = random_course.get_attribute('innerText')
        print(title)
        xpath = '//div[contains(@class,"course-listing-title") and contains(text(), "{}")]'.format(title)
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
        driver.quit()
ff = DynamicXPathFormat()
ff.test()
