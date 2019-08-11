from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys(object):

    def test(self):

        url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        xpath = "//div[@id='navbar']//a[@href='/sign_in']"

        login_link = driver.find_element(By.XPATH, xpath)
        login_link.click()
        # implicitly_wait - will try to find it first w/o wait, if it failed, will wait for provided amount of
        # seconds and try again. If it failed - failed, id not -success
        # this wait will applied to all the web elements we are trying to work on in this code.

        driver.implicitly_wait(5)

        email_field = driver.find_element(By.ID, 'user_email')
        email_field.send_keys('testing')
        password_field = driver.find_element(By.ID, 'user_password')
        password_field.send_keys('password')
        time.sleep(4)
        email_field.clear()
        time.sleep(4)
        email_field.send_keys('anna@gmail.com')
        login_button = driver.find_element(By.NAME, 'commit')
        login_button.click()
        time.sleep(5)
        driver.quit()

    def another_test(self):
        url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        practice_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/pages/practice"]')
        practice_link.click()
        driver.implicitly_wait(5)
        # linux_course_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/courses/94053"]')
        # linux_course_link.click()
        # watch_promo_link = driver.find_element(By.ID, '#watchpromo')
        hide_show_field = driver.find_element(By.ID, 'displayed-text')
        hide_show_field.send_keys('some text here')
        time.sleep(3)
        hide_button = driver.find_element(By.ID, 'hide-textbox')
        show_button = driver.find_element(By.ID, 'show-textbox')
        hide_button.click()
        time.sleep(3)
        show_button.click()
        time.sleep(3)
        hide_show_field.clear()
        time.sleep(3)
        driver.quit()

#ff = ClickAndSendKeys()
#ff.test()
#ff.another_test()

class ClickSendKeyChrome(object):

    def login(self):
        url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        login_link = driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        login_link.click()
        driver.implicitly_wait(10)
        user_email = driver.find_element(By.XPATH, "//input[@id='user_email']")
        user_email.send_keys("test")
        user_pw = driver.find_element(By.XPATH, "//input[@id='user_password']")
        user_pw.send_keys("test")
        driver.find_element(By.XPATH, "//input[@value='Log In']").click()
        time.sleep(7)
        driver.quit()

chrome = ClickSendKeyChrome()
chrome.login()



