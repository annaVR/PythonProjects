__author__ = 'anna'

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

print(set1.intersection(set2,set3))
print(set1.intersection(set2))
print(set1.intersection(set3))

print(set1.difference(set2))
print(set1 - set2)
print(set1.union(set2))