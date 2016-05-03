__author__ = 'anna'
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



