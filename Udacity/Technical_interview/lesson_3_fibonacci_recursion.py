__author__ = 'anna'
"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position < 2:
        return position
    else:
        result = get_fib(position - 2) + get_fib(position - 1)
        return result

def get_fib_2(position):
    if position < 2:
        return position
    else:
        first, second = 0, 1
        for fib_pos in range(position - 1):
            first, second = second, first + second
        return second


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
print('Iterative:')

print(get_fib_2(9))
print(get_fib_2(11))
print(get_fib_2(0))
