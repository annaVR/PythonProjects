__author__ = 'anna'

try:
    print(1//0)
except ZeroDivisionError as e:
    print('Error:', e)

try:
    print(int('b'))
except ValueError as e:
    print('Error:', e)

try:
    b = 1 + 'a'
except TypeError as e:
    print('Error:', e)

l = [i for i in range(11)]
try:
    a = l[20]
except IndexError as e:
    print('Error:', e)

d = {1: 'a', 2: 'b', 3: 'c'}
try:
    a = d[5]
except KeyError as e:
    print('Error:', e)

#catching ValueError and ZeroDivisionError while doing integer division

t = int(input().strip())
for test in range(t):
    try:
        a, b = map(int, input().strip().split())
        print(a//b)
    except ValueError as e:
        print('Error Code:', e)
    except ZeroDivisionError as b:
        print('Error Code:', b)
