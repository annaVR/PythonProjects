__author__ = 'anna'
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class DropdownSelect():

    def test_letskodeit(self):

        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        driver.implicitly_wait(5)

        element = driver.find_element(By.ID,'carselect')
        print(element.text)
        list_of_elements = Select(element)

        list_of_elements.select_by_index(1) #index starts from 0

        time.sleep(3)

        list_of_elements.select_by_value('honda')

        time.sleep(3)

        list_of_elements.select_by_visible_text('BMW')
        time.sleep(3)

        options_list = driver.find_elements(By.XPATH, '//select[@id="carselect"]//option')
        length_of_list = len(options_list)
        for i in range(length_of_list):
            elem = list_of_elements.select_by_index(i)
            time.sleep(3)
        print('Available options:')
        for option in list_of_elements.options:
            print(option)
        print('Selected options:')
        print(list_of_elements.all_selected_options)

        driver.quit()

    def test_expedia(self):
        url = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)

        element = driver.find_element(By.ID, "package-1-adults")
        options = Select(element)
        options_list = driver.find_elements(By.XPATH, '//select[@id="package-1-adults"]/option')
        length_of_list = len(options_list)
        for i in range(length_of_list):
            options.select_by_index(i)
            time.sleep(2)
        driver.quit()


#ff = DropdownSelect()
#ff.test_letskodeit()
#ff.test_expedia()


class DropdownSelectChrome(object):

    def test(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)

        dropdown = driver.find_element(By.XPATH, "//select[@id='carselect']")
        select = Select(dropdown)

        select.select_by_index(1)
        time.sleep(3)
        select.select_by_value('honda')
        time.sleep(3)
        select.select_by_visible_text('BMW')
        time.sleep(3)

        options = select.options
        for index in range(0, len(options)):
            element = select.select_by_index(index)
            time.sleep(3)

        driver.quit()

ch = DropdownSelectChrome()
ch.test()
