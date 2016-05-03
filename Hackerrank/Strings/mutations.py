__author__ = 'anna'
ls = list(input())
data =[i for i in input().split()]
ls[int(data[0])] = data[1]
print("".join(ls))