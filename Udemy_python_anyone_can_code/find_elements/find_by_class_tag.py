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

        list_elem_inputs = driver.find_elements_by_class_name('inputs')
        print(list_elem_inputs)
        for elem in list_elem_inputs:
            print('Text: {}'.format(elem.text))

        print('Anchor tags:')
        anchor_tag_element_list = driver.find_elements_by_tag_name('a')
        for elem in anchor_tag_element_list:
            print(elem.text)

        print('Buttons:')
        button_elements_list = driver.find_elements_by_tag_name('button')
        count = 0
        for elem in button_elements_list:
            count += 1
            print(elem.text)
        print(count)

#ff = FindByLinkPartialLink()
#ff.test()

class FindByClassTagChrome(object):

    def test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        elem_by_class = driver.find_element_by_class_name("displayed-class")
        elements_by_tag_name = driver.find_elements_by_tag_name("a ")
        if elem_by_class:
            print('Success 1')
        if elements_by_tag_name:
            print('Success 2')
            print(len(elements_by_tag_name))
        for element in elements_by_tag_name:
            print(element.text)
        driver.quit()
chrome = FindByClassTagChrome()
chrome.test()