from selenium import webdriver

class RunFFTests(object):

    def test(self):
        driver = webdriver.Firefox()
        driver.get('http://google.com')

ff = RunFFTests()
ff.test()