__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

class DynamicXPathFormat():

    def test(self):

        url = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        #login
        driver.find_element(By.LINK_TEXT, 'Login').click()
        driver.find_element(By.ID, 'user_email').send_keys('test@email.com')
        driver.find_element(By.ID, 'user_password').send_keys('abcabc')
        driver.find_element(By.NAME, 'commit').click()
        author = driver.find_element_by_xpath("//div[contains(text(),'Author')]//parent::div//"
                                              "button[@class='btn btn-default btn-lg btn-course-filter dropdown-toggle']")
        author.click()
        all_option = driver.find_element_by_xpath("//div[contains(text(),'Author:')]"
                                                  "//parent::div//a[text()='All']")
        all_option.click()
        time.sleep(2)

        #select random course from the list and open its link
        courses_list = driver.find_elements(By.CSS_SELECTOR, '.course-listing-title')
        for course in courses_list:
            print(course.text)
        random_course = random.choice(courses_list)
        title = random_course.get_attribute('innerText')
        index = 0
        for course in courses_list:
            title = course.get_attribute('innerText')
            print("This time I am clicking {}".format(title))
            xpath = '//div[contains(@class,"course-listing-title") and contains(text(), "{}")]'.format(title)
            driver.find_element(By.XPATH, xpath).click()
            time.sleep(2)
            driver.back()
        driver.quit()
ch = DynamicXPathFormat()
ch.test()
