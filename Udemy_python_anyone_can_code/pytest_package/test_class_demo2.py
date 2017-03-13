__author__ = 'anna'
#focus: make fixture return value and pass it to the TestClassDemo2 instance
import pytest
from .class_to_test import SomeClassToTest

#use fixtures for the whole class
@pytest.mark.usefixtures('module_set_up_level_to_test_a_class', 'method_set_up')
class TestClassDemo2():

    #create class_level fixture to prepare to run all tests: here to make an instance of a class we are testing and
    #maka it available to every method
    @pytest.fixture(autouse=True)
    def ClassSetup(self, module_set_up_level_to_test_a_class):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sum_numbers(2, 8)
        assert result == 20
        print('Running method A')

    def test_methodB(self):
        print('Running method B')