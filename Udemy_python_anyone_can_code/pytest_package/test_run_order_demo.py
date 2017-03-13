__author__ = 'anna'

import pytest

@pytest.mark.run(order=2)
def test_run_order_methodA(module_set_up, method_set_up):
    print('Running method A')

@pytest.mark.run(order=4)
def test_run_order_methodB(module_set_up, method_set_up):
    print('Running method B')

@pytest.mark.run(order=3)
def test_run_order_methodC(module_set_up, method_set_up):
    print('Running method C')

@pytest.mark.last
def test_run_order_methodD(module_set_up, method_set_up):
    print('Running method D')

@pytest.mark.run(order=1)
def test_run_order_methodE(module_set_up, method_set_up):
    print('Running method E')
