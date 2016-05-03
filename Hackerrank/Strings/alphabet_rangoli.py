__author__ = 'anna'


import string
alpha = string.ascii_lowercase
print(alpha)

abc = 'abcdefghijklmnopqrstuvwxyz'
size = int(input().strip())
sl = alpha[:size]
width = (size * 2 - 1) + (size * 2 - 2)
ind = None
flag = "index_down"


def print_row(index):
    st = sl[index:]
    print('{:-^{width}}'.format('-'.join(st[::-1]+st[1:]), width=width))

for line in range(size*2-1):
    if ind is None:
        ind = size - 1
        print_row(ind)
        ind -= 1
    elif ind > 0 and flag == "index_down":
        print_row(ind)
        ind -= 1
    elif ind == 0:
        flag = "index_up"
        print_row(ind)
        ind += 1
    else:
        print_row(ind)
        ind += 1
