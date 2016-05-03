__author__ = 'anna'
A = set(map(int, input().split()))
N = int(input())
s_bool = set()
for i in range(N):
    s = set(map(int, input().split()))
    s_bool.add(A.issuperset(s))
if len(s_bool) == 1 and True in s_bool:
    print(True)
else:
    print(False)