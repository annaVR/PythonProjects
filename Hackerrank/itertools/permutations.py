__author__ = 'anna'
from itertools import permutations
S, length = input().strip().split()
for elem in permutations(sorted(list(S)), int(length)):
    for item in elem:
        print(item, end='')
    print()
