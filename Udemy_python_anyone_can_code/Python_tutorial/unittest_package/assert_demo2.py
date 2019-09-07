__author__ = 'anna'

import unittest

class AssertDemo2(unittest.TestCase):

    def test_assert_in(self):

        a = 14
        b = [14, 56]
        self.assertIn(a, b, msg= 'a not in b')

    def test_count_equal(self):

        a = ['cat', 'dog']
        b = ['dog', 'cat']
        self.assertCountEqual(a, b, msg= 'a count not equal b')

    def test_assert_greater_equal(self):

        a = 3.11111111
        b = 3.11
        self.assertGreaterEqual(a, b, msg= 'a is not greater or equal to b')


if __name__ == "main":
    unittest.main(verbosity=2)