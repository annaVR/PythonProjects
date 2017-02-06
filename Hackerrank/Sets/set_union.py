__author__ = 'anna'

num_eng = int(input())
eng = set(map(int, input().split()))
num_fr = int(input())
fr = set(map(int, input().split()))
print(len(eng.union(fr)))