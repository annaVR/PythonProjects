__author__ = 'anna'

l = [[1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 2, 4, 4, 0],
     [0, 0, 0, 2, 0, 0],
     [0, 0, 1, 2, 4, 0]]

sums = []
len_column = 6
for row_index in range(len(l)-2):
    for column_index in range(len_column-2):
        top = sum(l[row_index][column_index:column_index + 3])
        middle = l[row_index + 1][column_index + 1]
        bottom = sum(l[row_index + 2][column_index:column_index + 3])
        print(top, middle, bottom)
        hourglasses = top + middle + bottom
        print(hourglasses)
        sums.append(hourglasses)
print(max(sums))





