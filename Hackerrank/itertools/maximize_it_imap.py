__author__ = 'anna'
from itertools import product
K = 3
M = 1000
l_ = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, -10]]

# K, M = map(int, input().strip().split())
# l_ = [map(int, input().strip().split()) for _ in range(K)]

l = [lis[1:] for lis in l_]
print(l)
combs = list(product(*l))
print(combs)
print(len(combs))
powers = [2 for i in range(len(l))]
print(powers)
max_sum = None
for comb in combs:
    summ = sum(map(pow, comb, powers)) % M
    if max_sum is None:
        max_sum = summ
    elif summ > max_sum:
        max_sum = summ
print(max_sum)


