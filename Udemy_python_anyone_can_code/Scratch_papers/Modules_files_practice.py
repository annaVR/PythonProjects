#modules
from math import sqrt
from math import ceil

class ModulesDemo():

    def builtin_modules(self):
        print(sqrt(100))
        print(ceil(1.1))


demo = ModulesDemo()
demo.builtin_modules()

# #files first method:
# my_list = [1, 2, 3]
# my_file = open('firstfile.txt', 'w')
# for item in my_list:
#     my_file.write(str(item) + '\n')
# my_file.close()
# my_list2 = [4, 5]
# my_file = open('firstfile.txt', 'a')
# for item in my_list2:
#     my_file.write(str(item) + '\n')
# my_file.close()
# my_file = open('firstfile.txt', 'r')
# print(my_file.read())
# my_file.close()
# my_file_line = open('firstfile.txt', 'r')
# print(my_file_line.readlines())
# my_file_line.close()

#files second method:
with open('withas.txt', 'w') as write:
    write.write('This is another way: with/as write and read')

with open('withas.txt', 'r') as read:
    print(read.read())
