__author__ = 'anna'


class SomeClassToTest():

    def __init__(self, value):
        self.value = value

    def sum_numbers(self, a, b):
        return a + b + self.value

    def multiply_numbers(self, a):
        return a * self.value