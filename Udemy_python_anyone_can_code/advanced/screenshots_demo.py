__author__ = 'anna'


import sys
sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/Udemy_python_anyone_can_code/tools')

from selenium import webdriver
#from custom_helpers import ff_setup
#from custom_helpers import take_screenshot
import time

class TakeScreenshots(object):

    def take_screenshot(self, driver):
        """
        Take screenshot of the current open web page
        :param driver:
        :return: none
        """
        file_name = time.strftime("%b:%d:%Y_%H:%M:%S", time.localtime(time.time())) + ".png"
        screenshot_directory = "/Users/annaromanovskaia/Desktop/{}".format(file_name)
        try:
            driver.save_screenshot(screenshot_directory)
            print("Screenshot saved to: {}".format(screenshot_directory))
        except NotADirectoryError:
            print("NotADirectoryError")

    def test(self):
        url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        login_link = driver.find_element_by_partial_link_text("Login")
        login_link.click()
        email = driver.find_element_by_id("user_email")
        email.send_keys("ab@email.com")
        password = driver.find_element_by_id("user_password")
        password.send_keys("ab")
        login_button = driver.find_element_by_name("commit")
        login_button.click()
        time.sleep(2)
        self.take_screenshot(driver)
        time.sleep(2)
        driver.quit()



ch = TakeScreenshots()
ch.test()