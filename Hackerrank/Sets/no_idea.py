__author__ = 'anna'

n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0
for elem in arr:
    if elem in a:
        happiness += 1
    elif elem in b:
        happiness -= 1
print(happiness)

# 3 2
# 1 5 3
# 3 1
# 5 7
