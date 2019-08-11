__author__ = 'anna'
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class BYDemo(object):

    def test(self):
        '''
        this method will find elements with anchor tag by the full text or partial text within the plain text field
        :return:
        '''

        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(url)

        element_by_id = driver.find_element(By.ID, 'carselect')
        print('Attribute:')
        print(element_by_id.get_attribute('id'))


        if element_by_id:
            print('Element by ID: {}'.format(element_by_id.text))

        element_by_xpath = driver.find_element(By.XPATH, "//button[@id='openwindow']")
        if element_by_xpath:
            print('Element by xpath: {}'.format(element_by_xpath.text))

        element_by_link_text = driver.find_element(By.LINK_TEXT, 'Sign Up')
        if element_by_link_text:
            print('Element by link text: {}'.format(element_by_link_text.text))

        print('Span elements:')
        span_elements = driver.find_elements(By.TAG_NAME, 'span')
        print(len(span_elements))
        for elem in span_elements:
            print(elem.text)

        driver.quit()

#ff = BYDemo()
#ff.test()

class ByDemoChrome(object):

    def test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        elem_by_id = driver.find_element(By.ID, 'name')
        elem_by_id.send_keys('Anna')
        elem_by_xpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        elements_by_class_name = driver.find_elements(By.CLASS_NAME, 'inputs')
        if elem_by_xpath:
            print("Element by XPath found")
        time.sleep(5)
        print("Element count: {}".format(elements_by_class_name.__len__()))
        count = 0
        for element in elements_by_class_name:
            count += 1
            print(count, element, element.text)
        elements_by_tag = driver.find_elements(By.TAG_NAME, 'legend')
        count = 0
        for element in elements_by_tag:
            count += 1
            print(count, element.text)

        driver.quit()

chrome = ByDemoChrome()
chrome.test()



