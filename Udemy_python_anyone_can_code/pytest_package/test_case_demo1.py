__author__ = 'anna'

import pytest


@pytest.fixture()
def set_up():
    print('Once before every method')


def test_method1(set_up):
    print('Running method 1')


def test_method2(set_up):
    print('Running method 2')







