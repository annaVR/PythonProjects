__author__ = 'anna'

from collections import OrderedDict
n = int(input())
prod_ord_dict = OrderedDict()
for i in range(n):
    inp = input().split()
    for j in range(1, len(inp)-1):
        try:
            int(inp[j])
        except:
            inp[0] += (" " + inp[j])
            del inp[j]
    if inp[0] in prod_ord_dict:
        prod_ord_dict[inp[0]] += int(inp[1])
    else:
        prod_ord_dict[inp[0]] = int(inp[1])

for k, v in prod_ord_dict.items():
    print(k, v)

#better:

d = OrderedDict()
for _ in range(int(input())):
    name, space, price = input().rpartition(' ')
    d[name] = d.get(name, 0) + int(price)
for item, price in d.items():
    print(item, price)
