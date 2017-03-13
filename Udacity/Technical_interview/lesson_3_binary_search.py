__author__ = 'anna'

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python_tutorial list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    if input_array and value:
        result = None
        min_bound = 0
        max_bound = len(input_array)-1
        if len(input_array) % 2 == 0:
            target = (max_bound-1)//2
            while min_bound < max_bound:
                result = input_array[target]
                if result == value:
                    return target
                elif result < value:
                    min_bound = target + 1
                    target = (min_bound + max_bound - 1)//2
                elif result > value:
                    max_bound = target - 1
                    target = (min_bound + max_bound)//2
                if min_bound == max_bound:
                    result = input_array[target]
                    if result == value:
                        return target
            return '-1'
        elif len(input_array) % 2 != 0:
            target = (max_bound)//2
            while min_bound <  max_bound:
                result = input_array[target]
                if result == value:
                    return target
                elif result < value:
                    min_bound = target + 1
                    target = (min_bound + max_bound - 1)//2
                elif result > value:
                    max_bound = target - 1
                    target = (min_bound + max_bound - 1)//2
                if min_bound == max_bound:
                    result = input_array[target]
                    if result == value:
                        return target
            return '-1'


test_list = [1,3,9,11,15,19,29,30]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print()
test_list_2 = [1, 5, 7, 10, 11, 14, 20, 48, 60]
test_val3 = 3
test_val4 = 20
test_val5 = 68
test_val6 = -2
print(binary_search(test_list_2, test_val3))
print(binary_search(test_list_2, test_val4))
print(binary_search(test_list_2, test_val5))
print(binary_search(test_list_2, test_val6))