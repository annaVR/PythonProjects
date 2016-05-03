__author__ = 'anna'
import functools
s = set("Anna")
print(s)
print(list(range(6)))
s = set(range(6))
print(s)
d = {"Anna": 5, "Masha": 6}
print(set(d))
l = ['January', 'February', 'March', 'March']
print(list(enumerate(l,  start=1)))
print(set(enumerate(l, start=1)))
print(set(enumerate(set(l), start=1)))
st = {1, 3, 4}
print(sum(st))
print()
def add(x, y):
    return x+y

a = [1, 2, 3, 2]
b = functools.reduce(add, a)
print(b)

l = ['dsf', '1', 'dfsdfs','4']
print('{}'.format(''.join(l)))

f = lambda x, y: x-y
print(f(10,6))





