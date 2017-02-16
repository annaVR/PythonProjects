__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By

class Wrappers():

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element
    #using our function get_by_type in this function
    def is_element_present(self, locator_type, locator):
        try:
            element = self.driver.find_element(self.get_by_type(locator_type), locator)
            return True
        except:
            return False


    #using class By.type as an argument
    def is_element_present_list_method(self, by_type, locator):
        elements_list = self.driver.find_elements(by_type, locator)
        if len(elements_list) > 0:
            return True
        else:
            return False