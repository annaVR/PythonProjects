__author__ = 'anna'
from itertools import groupby

l = list(map(int, input().strip()))
for k, group in groupby(l, lambda k: k):
    print((len(list(group)), k), end=' ')