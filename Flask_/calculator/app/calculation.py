__author__ = 'anna'
import re
from collections import deque

def calculation(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        return first_number/second_number

def calculation_from_string_data(string_data):
    string_data = string_data
    numbers = re.findall('(\d+)', string_data)
    operations = re.findall('(\+|\-{1})', string_data)
    ls = [None]*(len(numbers) + len(operations))
    ls[::2] = numbers
    ls[1::2] = operations
    result = int(ls[0])
    ls = ls[1:]
    queue = deque(ls)
    while queue:
        operation = queue.popleft()
        number = int(queue.popleft())
        if operation == '+':
            result += number
        elif operation == '-':
            result -= number
    return result