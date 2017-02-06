__author__ = 'anna'
from itertools import product
A = map(int, input().strip().split())
B = map(int, input().strip().split())
for _ in product(A, B):
    print(_, end=' ')