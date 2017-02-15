from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementState(object):

    def test(self):
        url = 'http://www.google.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        driver.implicitly_wait(3)

        e1 = driver.find_element(By.ID, "lst-ib")
        print(e1.is_enabled())

        el2 = driver.find_element(By.ID, "gs_taif0")
        print(el2.is_enabled())

        el3 = driver.find_element(By.ID, "gs_htif0")
        print(el3.is_enabled())

        e1.send_keys('Apple\n')
        time.sleep(5)

        driver.quit()

ff = ElementState()
ff.test()