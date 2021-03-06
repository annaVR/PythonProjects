__author__ = 'anna'
from selenium import webdriver

class FindByIdName(object):

    def test(self):

        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(url)
        element_id = driver.find_element_by_id('name')
        element_name = driver.find_element_by_name('show-hide')
        if element_id and element_name:
            print(element_id, element_name)


#ff = FindByIdName()
#ff.test()

class FindByIDNameChrome(object):

    def test(self):

        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        element_by_id = driver.find_element_by_id('name')
        element_by_name = driver.find_element_by_name('enter-name')
        if element_by_id and element_by_name:
            print('Success')

chrome = FindByIDNameChrome()
chrome.test()
