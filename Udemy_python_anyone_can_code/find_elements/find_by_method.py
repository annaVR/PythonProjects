__author__ = 'anna'
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

ff = BYDemo()
ff.test()
