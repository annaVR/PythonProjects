__author__ = 'anna'

t = {'Anna', 'Masha', 'Sergey'}
s = {'Anna', 'Masha'}

if s.issubset(t) and s != t:
    print("s is subset of t")
else:
    print('s is not subset of t')

print(s.issubset(t))

print(s.union(t))

print(s.difference(t))

print(t.difference(s))

s = set()
for i in range(1,5):
    s.add(i * i)
    s.add(-i)
print(s)

s = set()
for i in range(0, 20, 2):
    s.add(i)
print(s)
for i in range(0, 20, 3):
    s.discard(i)
print(s)

