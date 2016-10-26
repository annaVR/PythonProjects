__author__ = 'anna'

import dis
import random

def swap(a, b):
    return b, a

def partition(l, start, end):
    pivot = l[end]
    p_index = start
    for i in range(start, end):
        if l[i] <= pivot:
            l[p_index], l[i] = swap(l[p_index], l[i])
            p_index += 1
    l[p_index], l[end] = swap(l[p_index], l[end])
    return p_index

def quick_sort(l, start, end):
    if start < end:
        p_index = partition(l, start, end)
        quick_sort(l, start, p_index - 1)
        quick_sort(l, p_index + 1, end)

def main():
    l = [5, 7, 3, 6, 79, 27, 4]
    quick_sort(l, 0, 6)
    print('First:', l)
    l_2 = list(range(1, 101))
    print(l_2)
    random.shuffle(l_2)
    print(l_2)
    quick_sort(l_2, 0, 99)
    print('Second:', l_2)

main()
