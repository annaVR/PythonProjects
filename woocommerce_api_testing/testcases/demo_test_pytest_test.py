__author__ = 'anna'


def my_subtract(a, b):
    return a - b


def my_power(a, b):
    return a ** b


def test_tc1_my_subtract():
    assert my_subtract(10, 2) ==8, 'TC1 difference is not 8.'


def test_tc2_my_subtract():
    assert my_subtract(23, 3) == 20, 'TC2 difference is not 20.'


def test_tc3_my_power():
    assert my_power(2, 4) == 16, 'TC3 power is not 16.'


def test_tc4_my_power():
    assert my_power(3, 2) == 9, 'TC5 power is not 27.'
