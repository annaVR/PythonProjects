__author__ = 'anna'
t = tuple()
nm = int(input())
inp = input()
ls_inp = [int(i) for i in inp.split()]
t = tuple(ls_inp)
print (hash(t))
