__author__ = 'anna'

import unittest

class AssertDemo(unittest.TestCase):

    def test_assert_true_false(self):
        a = True
        self.assertTrue(a, 'a is not True')
        b = False
        self.assertFalse(b, 'b is not False')

    def test_assert_equal(self):
        a = 1
        b = 1

        self.assertEqual(a, b, msg='a is not equal to b')

    def test_assertGreater(self):
        a = 36
        b = 35

        self.assertGreater(a, b, msg="a is not greater then b")

if __name__ == '__main__':
    unittest.main(verbosity=2)
