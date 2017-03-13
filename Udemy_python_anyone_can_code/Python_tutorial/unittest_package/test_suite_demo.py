__author__ = 'anna'

import unittest
from test_case_demo1 import TestCaseDemo1
from test_case_demo2 import TestCaseDemo2
from assert_demo import AssertDemo

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)

test_suit = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(test_suit)
