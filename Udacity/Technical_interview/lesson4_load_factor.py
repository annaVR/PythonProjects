__author__ = 'anna'

import random


l = list(range(0, 10000, 5))


new_list = random.sample(l, 100)
print(new_list)

d = {}
values = []

for i in range(0, 107):
    d[i] = []
print(sorted(d))

for item in new_list:
    key = item % 107
    d[key].append(item)

count = 0
for key in sorted(d):
    count += 1
    print(key, d[key])
print('Count', count)
