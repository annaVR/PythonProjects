__author__ = 'anna'
n, l = int(input().strip()), list(map(int, input().strip().split()))
print(all([all(elem > 0 for elem in l), any(map(lambda x: str(x) == str(x)[::-1], l))]))

# print(all(elem > 0 for elem in l))
# print(any(list(map(int, str(elem))) == list(reversed(list(map(int, str(elem))))) for elem in l))
#
# c = -67
# b = list(map(int, str(abs(c))))
# print(b)
# print(list(reversed(b)))
# print(all([True, True]))


print(list(map(lambda x: str(x) == str(x)[::-1], l)))

print([False, any(map(lambda x: str(x) == str(x)[::-1], l))][all(map(lambda x: x > 0, l))])
print([False, False] [True])
