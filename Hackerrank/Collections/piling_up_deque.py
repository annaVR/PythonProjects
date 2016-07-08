__author__ = 'anna'
from collections import deque
for test in range(int(input().strip())):
    num_cubes = int(input().strip())
    d = deque(map(int, input().strip().split()))
    d_length = len(d)
    stack = [0]
    right = None
    left = None
    while len(stack) == 1 or len(d) >= 2 and d[0] <= stack[-1] and d[-1] <= stack[-1]:
        left = d.popleft()
        print(left)
        right = d.pop()
        print(right)
        if left == right:
            stack.append(left)
            stack.append(right)
            print(stack)
        elif left > right:
            stack.append(left)
            d.append(right)
        elif left < right:
            stack.append(right)
            d.appendleft(left)

    if len(d) > 1:
        print('False')
    elif len(d) == 1:
        last = d.pop()
        if last <= stack[-1]:
            stack.append(last)
            print('True')
        else:
            print('False')
    elif len(d) == 0:
        print('True')


