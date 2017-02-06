__author__ = 'anna'
a, b = set(input("Type a string:")), set(input("Type a string:"))
print("union:", a.union(b))
print("a.difference(b):", a.difference(b))
print('symmetric diff', a.symmetric_difference(b))