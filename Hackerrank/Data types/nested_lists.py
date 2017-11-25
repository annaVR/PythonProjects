__author__ = 'anna'

from operator import itemgetter

# n = int(input())
# l = list()
# lst = list()
# for i in range(n):
#     name = input()
#     score = float(input())
#     lst = [name, score]
#     l.append(lst)
records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
def my_f(x):
    return x[1]
grades_l = list(map(my_f, records))
print(grades_l)
grades_l.sort()
print(grades_l)
my_set = set(grades_l)
uniq_list=list(my_set)
uniq_list.sort()
sec_low_grade=uniq_list[1]
print(sec_low_grade)
# def my_f1(x):
#     return x[0]
#sec_grades = list(map(my_f1(),records))


records_1 = [i for i in records if i[1]==sec_low_grade]
records_1.sort()
for record in records_1:
    print(record[0])


print('Second solution:')

records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

s_records = sorted(records, key=itemgetter(1,0))
print(s_records)
for i in range(1, len(s_records)):
    if s_records[i][1] == s_records[i-1][1] and s_records[i][1] == s_records[i+1][1]:
        continue
    elif s_records[i][1] == s_records[i-1][1] and s_records[i][1] < s_records[i+1][1]:
        second_larg_grade = s_records[i + 1][1]
        break
    else:
        second_larg_grade = s_records[i][1]
        break
print(second_larg_grade)
for record in s_records:
    if record[1] == second_larg_grade:
        print(record[0])

print('Second solution2:')

records = [['Prashant', 32], ['Pallavi', 36], ['Dheeraj', 39], ['Shivam', 40]]

s_records = sorted(records, key=itemgetter(1,0))
print(s_records)
for i in range(1, len(s_records)):
    if s_records[i][1] == s_records[i-1][1] and s_records[i][1] == s_records[i+1][1]:
        continue
    elif s_records[i][1] == s_records[i-1][1] and s_records[i][1] < s_records[i+1][1]:
        second_larg_grade = s_records[i + 1][1]
        break
    else:
        second_larg_grade = s_records[i][1]
        break
print(second_larg_grade)
for record in s_records:
    if record[1] == second_larg_grade:
        print(record[0])




