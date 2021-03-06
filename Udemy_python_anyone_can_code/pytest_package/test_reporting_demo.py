__author__ = 'anna'

# pip3 install pytest-html and when we run the file via py.test we pass the name
# of the file where we want to save the html report to the kwarg --html=filepath.html. By default it saves in the module folder

import pytest
from .class_to_test import SomeClassToTest

#use fixtures defined on conftest.py for the whole class
@pytest.mark.usefixtures('module_set_up_level_to_test_a_class', 'method_set_up')
class TestReportingDemo():


    @pytest.fixture(autouse=True)
    def ClassSetup(self, module_set_up_level_to_test_a_class):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sum_numbers(2, 8)
        assert result == 20
        print('Running method A')

    def test_methodB(self):
        result = self.abc.sum_numbers(2, 8)
        assert result == 30
        print('Running method B')