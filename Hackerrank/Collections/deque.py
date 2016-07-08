
from collections import deque
que = deque()
for _ in range(int(input())):
    method, _, args = input().strip().partition(" ")
    print(method)
    print(_)
    print(args)
    getattr(que, method)(*args.split())
print('que', *list(que))




# for _ in range((int(input()))):
#     oper, space, num = input().strip().partition(' ')


