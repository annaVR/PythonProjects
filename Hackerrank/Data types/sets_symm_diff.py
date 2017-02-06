__author__ = 'anna'

lst = list()
for round in range(0, 2):
    n = int(input())
    str = input()
    ls_str = str.split()
    ls = list(map(int,ls_str))
    st = set(ls)
    lst.append(st)
st1 = lst[0]
st2 = lst[1]
diff = st1.symmetric_difference(st2)
diff_list = list(map(int, diff))
for item in sorted(diff_list):
    print(item)
