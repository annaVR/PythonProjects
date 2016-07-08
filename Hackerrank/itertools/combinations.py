__author__ = 'anna'
from itertools import combinations
from itertools import combinations_with_replacement
s, lengths = input().strip().split()
sorted_list = sorted(list(s))
count = 0
for length in range(1, int(lengths)+1):
    for item in combinations(sorted_list, length):
        print(''.join(item))
        count += 1
    print('Count:', count)
    count = 0
for length in range(1, int(lengths)+1):
    for item in combinations_with_replacement(sorted_list, length):
        print(''.join(item))
        count += 1
    print('Count', count)
    count = 0
