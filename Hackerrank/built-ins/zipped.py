__author__ = 'anna'
# n, x = map(int, input().strip().split())
# mark_sheet = [list(map(float, (input().strip().split()))) for subj in range(x)]

n, x = float(5), float(3)
mark_sheet = [[89.0, 90.0, 78.0, 93.0, 80.0], [90.0, 91.0, 85.0, 88.0, 86.0], [91.0, 92.0, 83.0, 89.0, 90.5]]
print(mark_sheet)
stud_scores = list(zip(*mark_sheet))
print(stud_scores)
averages = [print('{:.1f}'.format(sum(student) / float(x))) for student in stud_scores]
print(averages)

# same: readable:
# averages = [sum(student)/ float(x) for student in stud_scores]
# for average in averages:
#     print('{:.1f}'.format(average))
