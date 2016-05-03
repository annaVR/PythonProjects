__author__ = 'anna'

from collections import defaultdict
# n, m = map(int, input().split())
# a = [input() for i in range(n)]
# b = [input() for i in range(m)]
# a_dict = defaultdict(list)
# for v in a:
#     a_dict[v].append(a.index(v)+1)
# for letter in b:
#     if a_dict[letter]:
#         values = map(str, a_dict[letter])
#         print(' '.join(values))
#     else:
#         print(-1)

n, m = 5, 2
a = list(map(str, "aabab"))
b = 'abc'
a_dict = defaultdict(list)
for i in range(len(a)):
    a_dict[a[i]].append(i+1)
print(a_dict)
for letter in b:
    if a_dict[letter]:
        values = map(str, a_dict[letter])
        print(' '.join(values))
    else:
        print(-1)
