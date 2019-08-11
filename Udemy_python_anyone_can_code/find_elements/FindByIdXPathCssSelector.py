__author__ = 'anna'
from selenium import webdriver

class FindByXPathCss(object):

    def test(self):

        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(url)

        element_xpath = driver.find_element_by_xpath("//input[@id='displayed-text']") # removed .
        # from the beginning of xpath, replaced * by 'input' - the tag name
        element_css = driver.find_element_by_css_selector('#displayed-text')

        if element_xpath == element_css:
            print('Element found by xpath and by css selector is the same element.')


#ff = FindByXPathCss()
#ff.test()

class FindByXPathCssChrome(object):

    def test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)

        elem_by_xpath = driver.find_element_by_xpath('//input[@id="name"]')
        try:
            elem_by_css = driver.find_element_by_css_selector('#named')
        except:
            print('Exception happend on second find')
            elem_by_css = None
        if elem_by_xpath:
            print('First element found')
        if elem_by_xpath and elem_by_css:
            print('Success')
        driver.quit()
chrome = FindByXPathCssChrome()
chrome.test()
