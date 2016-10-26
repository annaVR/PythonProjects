__author__ = 'anna'

#O(n^2)
def reverse_list(l):
    count = 0
    for i in range(len(l)-1):
        elem = l.pop()
        l.insert(count, elem)
        count += 1
    return l

l = ['n', 'i', 'v', 'e', 'a']
print(reverse_list(l))

l_2 = list(range(0, 16))
print(reverse_list(l_2))
print()
#O(n):

def reverse_list(l):
    beginning = 0
    end = len(l) - 1
    for i in range(len(l)//2):
        temp = l[beginning]
        l[beginning] = l[end]
        l[end] = temp
        beginning += 1
        end -= 1
    return l

l = ['n', 'i', 'v', 'e', 'a']
print(reverse_list(l))

l_2 = list(range(0, 16))
print(reverse_list(l_2))

