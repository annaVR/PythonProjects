__author__ = 'anna'
from itertools import combinations_with_replacement
s, k = input().strip().split()
sorted_list = sorted(list(s))
for elem in combinations_with_replacement(sorted_list, int(k)):
    print(''.join(elem))