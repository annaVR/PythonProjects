__author__ = 'anna'

n = int(input())
s = set(map(int, input().split()))
num_comm = int(input())
for line in range(num_comm):
    line = input().split()
    if len(line) == 1:
        s.pop()
    elif line[0] == 'remove':
        s.remove(int(line[1]))
    elif line[0] == 'discard':
        s.discard(int(line[1]))
print(sum(s))