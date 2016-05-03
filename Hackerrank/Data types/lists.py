__author__ = 'anna'
l = []
lines = int(input())
for line in range(0, lines):
    inp = input()
    ls_input = inp.split()
    command = ls_input[0]
    if command == "insert":
        index = int(ls_input[1])
        value = int(ls_input[2])
        l.insert(index,value)
    elif command == "print":
        print (l)
    elif command == "remove":
        value = int(ls_input[1])
        l.remove(value)
    elif command == "append":
        value = int(ls_input[1])
        l.append(value)
    elif command == "sort":
        l.sort()
    elif command == "pop":
        l.pop()
    elif command == "reverse":
        l.reverse()


