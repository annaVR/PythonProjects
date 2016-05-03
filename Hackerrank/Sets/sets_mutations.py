__author__ = 'anna'

num_a = int(input())
a = set(map(int, input().split()))
operations = int(input())
for operation in range(operations):
    operation = input().split()[0]
    set_2 = set(map(int, input().split()))
    if operation == 'intersection_update':
        a.intersection_update(set_2)
    elif operation == 'update':
        a.update(set_2)
    elif operation == 'symmetric_difference_update':
        a.symmetric_difference_update(set_2)
    elif operation == 'difference_update':
        a.difference_update(set_2)
print(sum(a))

