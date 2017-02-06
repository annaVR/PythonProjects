__author__ = 'anna'
from collections import namedtuple
# num = int(input())
# Spreadsheet = namedtuple('Spreadsheet', ','.join(input().split()))
# summ = 0
# for i in range(num):
#     pos_arg = input().split()
#     print(pos_arg)
#     record_tuple = Spreadsheet(pos_arg)
#     summ += int(record_tuple.MARKS)
# print(summ)
num = 2
inp = 'ID         MARKS      NAME       CLASS'
cleaned_inp = ','.join(inp.split())
print('Cleaned input: {!r}'.format(cleaned_inp))
Spreadsheet = namedtuple('Spreadsheet', cleaned_inp)
example = Spreadsheet('a', 'b', 'c', 1)
print(example)
summ = 0
for i in range(num):
    pos_arg = input().split()
    record_tuple = Spreadsheet(*pos_arg)
    summ += int(record_tuple.MARKS)
print(summ)