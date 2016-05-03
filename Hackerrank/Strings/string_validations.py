__author__ = 'anna'
st = 'qA2'
l_1 = [st[i].isalnum() for i in range(len(st))]
l_2 = [st[i].isalpha() for i in range(len(st))]
l_3 = [st[i].isdigit() for i in range(len(st))]
l_4 = [st[i].islower() for i in range(len(st))]
l_5 = [st[i].isupper() for i in range(len(st))]
ls = [i for i in (l_1, l_2, l_3, l_4, l_5)]
print(ls)
for item in ls:
    if True in item:
        print("True")
    else:
        print("False")