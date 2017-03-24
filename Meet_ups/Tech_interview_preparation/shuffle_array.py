__author__ = 'anna'
import random

def shuffle_array(arr):
    counter = len(arr)
    print('Counter:', counter)

    for turn in range(counter):
        i = random.choice(range(0, counter))
        print('i', i)

        counter -= 1
        temp = arr[counter]
        arr[counter] = arr[i]
        arr[i] = temp

        print(arr)
    print(arr)

arr = [1, 45, 84, 4]
shuffle_array(arr)
