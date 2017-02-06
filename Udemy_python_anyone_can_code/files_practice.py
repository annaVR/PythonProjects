__author__ = 'anna'

f_handle = open('/home/anna/Documents/Test/first_file.txt', 'w')

l = list(range(0, 10, 2))

print(l)


for item in l:
    f_handle.write(str(item) + '\n')

f_handle.close()

f_handle = open('/home/anna/Documents/Test/first_file.txt', 'r')

print(f_handle.read())

f_handle.seek(0, 0)
print('Using readline and for loop:')
for i in range(len(l)):
    print(f_handle.readline(), end='')

f_handle.seek(0, 0)

print('Using readline and while loop')

while True:
    line = f_handle.readline()
    if len(line) == 0:
        break
    print(line, end='')

f_handle.seek(0, 0)
print('Using readlines:')

for line in f_handle.readlines():
    print(line, end='')
f_handle.seek(0, 0)

print('The whole readlines object-list:')

print(f_handle.readlines())

f_handle.seek(0, 0)
print('Iterating through a file:')
i = 0
for line in f_handle:
    print(line, end='')
    i += 1
print('Total number of lines: {}'.format(i))

f_handle.close()

f_handle = open('/home/anna/Documents/Test/first_file.txt', 'w')
f_handle.truncate()
f_handle.close()

print('Second part:')

fruits = ['apple', 'pear', 'watermelon', 'grape']

f_handle = open('/home/anna/Documents/Test/fruits.txt', 'w')

for fruit in fruits:
    f_handle.write(str(fruit) + '\n')
f_handle.close()

print('Sorting the content with readlines:')

f_handle = open('/home/anna/Documents/Test/fruits.txt', 'r')

for item in sorted(f_handle.readlines()):
    print(item, end='')

f_handle.seek(0, 0)

print('Turning the whole file in one string, truncating spaces:')

l = f_handle.read().split()
print(''.join(l))

f_handle.seek(0, 0)

s = f_handle.read().replace('\n', '')
print(s)


f_handle.close()
