__author__ = 'anna'

# n, m = 5, 3
# table = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
# # n, m = map(int, input().strip().split())
# # table = [[map(int, input().strip().split())] for inp in range(n)]
# # i = int(input().strip())
# i = 1
# table_sorted = sorted(table, key=lambda k: k[i])
# for item in table_sorted:
#     print(*item)

n, m = map(int, input().strip().split())
table = [list(map(int, input().strip().split())) for _ in range(n)]
print(table)
i = int(input().strip())
print(i)
table_sorted = sorted(list(table), key=lambda k: k[i])
for item in table_sorted:
    print(*item)