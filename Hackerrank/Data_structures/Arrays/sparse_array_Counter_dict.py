__author__ = 'anna'

from collections import Counter
n = int(input().strip())
array_of_strings = [input().strip() for inp in range(n)]
q = int(input().strip())
array_of_queries = [input().strip() for inp in range(q)]
cnt = Counter(array_of_strings)
for query in array_of_queries:
    if query in cnt:
        print(cnt[query])
    elif query not in cnt:
        print(0)

# input:
# 4
# aba
# baba
# aba
# xzxb
# 3
# aba
# xzxb
# ab
