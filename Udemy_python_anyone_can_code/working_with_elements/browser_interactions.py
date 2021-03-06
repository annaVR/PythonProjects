__author__ = 'anna'

from selenium import webdriver
import time

class BrowserInteractions(object):

    def test(self):
        driver = webdriver.Firefox()
        #it is better to max window before open the url
        driver.maximize_window()
        driver.get('https://letskodeit.teachable.com/p/practice')

        print(driver.title)

        print(driver.current_url)

        print('Refresh for the first time:')
        driver.refresh()

        print('Refresh for the second time:')
        driver.get(driver.current_url)

        print(driver.page_source)

        driver.get('http://www.thegeekstuff.com/2010/08/bash-shell-builtin-commands/')

        driver.back()

        driver.forward()

        #driver.close()

        driver.quit()

#ff = BrowserInteractions()
#ff.test()


class InterractionsChrome(object):

    def test(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        print('Page title: {}'.format(driver.title))
        print('Url: {}'.format(driver.current_url))

        driver.refresh()
        time.sleep(3)
        driver.get(driver.current_url)
        print("Open another URL")
        driver.get('https://google.com')
        print('Url: {}'.format(driver.current_url))
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        page_source = driver.page_source
        driver.quit()

chrome = InterractionsChrome()
chrome.test()


