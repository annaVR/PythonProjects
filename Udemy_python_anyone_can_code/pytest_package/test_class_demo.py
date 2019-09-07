__author__ = 'anna'

import pytest
from .class_to_test import SomeClassToTest

#use fixtures defined on conftest.py for the whole class
@pytest.mark.usefixtures('module_set_up_level_to_test_a_class', 'method_set_up')
class TestClassDemo():

    #create class_level fixture to prepare to run all tests: here to make an instance of a class we are testing and
    #make it available to every method -
    # - so, we are making def ClassSetup: self.abc == SomeClass.. available to all the class test_methods
    @pytest.fixture(autouse=True)
    def ClassSetup(self):
        self.abc = SomeClassToTest(35)

    def test_methodA(self):
        result = self.abc.sum_numbers(2, 8)
        assert result == 45
        print('Running method A')

    def test_methodB(self):
        result = self.abc.multiply_numbers(4)
        assert result == 146
        print('Running method B')