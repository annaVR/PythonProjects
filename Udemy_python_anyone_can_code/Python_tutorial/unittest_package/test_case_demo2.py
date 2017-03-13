__author__ = 'anna'

import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('run once before all tests')
        print('#' * 30)

    def setUp(self):
        print('run once before every test')

    def test_methodA(self):
        print('Running methodA')

    def test_methodB(self):
        print('Running methodB')

    def tearDown(self):
        print('run once after every test')

    @classmethod
    def tearDownClass(cls):
        print('#' * 30)
        print('run once after all tests')


if __name__ =='__main__':
    unittest.main(verbosity=2)
