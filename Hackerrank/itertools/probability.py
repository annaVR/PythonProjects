__author__ = 'anna'

from itertools import combinations

l = ['a', 'a', 'c', 'd', 'd', 'd']
l_length = len(l)
indices_number = 2
comb = list(combinations(range(l_length), indices_number))
print(comb)
a_indices = []
for i in range(len(l)):
    if l[i] == 'a':
        a_indices.append(i)
print(a_indices)

flag = "False"
count = 0
for elem in comb:
    for i in a_indices:
        if flag == 'False':
            if i in elem:
                flag = "True"
    if flag == "True":
        count += 1
        flag = 'False'
print('{:.3f}'.format(count/len(comb)))