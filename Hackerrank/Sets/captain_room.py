__author__ = 'anna'
k = int(input())
list_rooms = list(map(int, input().split()))
s = set(list_rooms)
for item in s:
    list_rooms.remove(item)
s_2 = set(list_rooms)
for i in s.difference(s_2):
    print(i)
