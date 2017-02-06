__author__ = 'anna'

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input().rstrip())):
    word = input().rstrip()
    d[word] = d.get(word, 0) + 1
print(len(d))
for occ in d.values():
    print(occ, end=" ")
