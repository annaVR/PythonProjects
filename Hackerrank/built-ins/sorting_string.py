__author__ = 'anna'
import string
import timeit
l = list(range(99999,-1,-1))
m = list(range(0,100000,1))

#l = list(string.ascii_letters)
#odd = [i for i in range(1, 10, 2)]
#even = [i for i in range(2, 9, 2)]
#l.extend(map(str, odd))
#l.extend(map(str, even))
#print(l)
def zz():
    hash_map = {}
    for item in m:
        hash_map[item] = m.index(item)
#print(hash_map)
    s_sorted = sorted(l, key=lambda k: hash_map[k])
    print(s_sorted[0])
    print(len(s_sorted), sep='')

print(timeit.timeit(zz,number=1))

def zz_2():
    s_sorted = sorted(l, key=lambda k: m.index(k))
    print(s_sorted[0])
    print(len(s_sorted))

print(timeit.timeit(zz_2, number=1))

# # the bad way using tuples:
# s = 'Sorting1234'
# print(*(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) %
# 2 == 0, x.isupper(), x.islower(), x))), sep='')
#
#
# def importance(elem):
#     return(elem.isdigit(), elem.isdigit() and int(elem) % 2 == 0, elem.isupper(), elem.islower(), elem)
#
#
# for k in s:
#     print(importance(k))
#
# l = [importance(k) for k in s]
# print(l)
#
# print(sorted(l))
# for elem in sorted(l):
#     print(elem[4], sep='', end='')
#
#
# print()
# s_2 = ' sTring12345'
#
# #print string:
# #first - digits muplitiple of 5
# #second- digits multiple of 3
# #third - the rest digits
# #forth - blank spaces: " "
# #fifth - lowercase letters
# #sixth - uppercase
# #seventh - letter 'g
# def importance_2(x):
#     return (x == 'g', x.isupper(), x.islower(), x ==' ', x.isdigit()
# and int(x) % 5 != 0,  x.isdigit() and int(x) % 3 != 0, x)
# l_2 = [importance_2(k) for k in s_2]
# for i in l_2:
#     print(i)
# print()
# print(*(sorted(l_2)), sep='\n')
# print(*(sorted(s_2, key=lambda x: (x == 'g', x.isupper(), x.islower(),
# x ==' ', x.isdigit() and int(x) % 5 != 0,  x.isdigit() and int(x) % 3
# != 0, x))))
