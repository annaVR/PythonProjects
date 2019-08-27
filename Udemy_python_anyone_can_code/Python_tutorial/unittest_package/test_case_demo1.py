__author__ = 'anna'
import unittest


class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        print('Run once before every test')

    #tests methods should start with word 'test'
    def test_method1(self):
        print('Running method1')

    def test_method2(self):
        print('Running method2')

    def tearDown(self):
        print('Run once after every test')


if __name__ =='__main__':
    unittest.main(verbosity=2)