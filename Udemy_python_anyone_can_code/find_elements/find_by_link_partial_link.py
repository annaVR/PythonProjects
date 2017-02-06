__author__ = 'anna'
from selenium import webdriver

class FindByLinkPartialLink(object):

    def test(self):
        '''
        this method will find elements with anchor tag by the full text or partial text within the plain text field
        :return:
        '''

        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(url)

        element_link = driver.find_element_by_link_text('Practice')
        element_partial_link = driver.find_element_by_partial_link_text('Prac')
        if element_link == element_partial_link:
            print('Two element found are the same element.')


ff = FindByLinkPartialLink()
ff.test()
