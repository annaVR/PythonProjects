# def summ(x, y, z):
#     print(x + y + z)
#
# def change_sum(*args):
#     args = list(args)
#     args[0] = 0
#     args[1] = 100
#     summ(*args)
# change_sum(10, 10, 10)
#
# def func1(x, y, z):
#     print(x, end=' ')
#     print(y, end=' ')
#     print(z)
#
# def changed_func1(*args):
#     args = list(args)
#     args[2] = 'Boo!'
#     func1(*args)
#
# l = ['One', 'Two', 'Three']
# changed_func1(*l)
# changed_func1('jdfj','hefah', 5)
#
# L = [num for num in range(16)]
#
# print(*L)
#
# multiples_of_3 = (not (i % 5) for i in range(1, 10))
# # print(list(multiples_of_3))
# print(any(multiples_of_3))
# print(list(multiples_of_3))
# print('Next:')

def digit_sum(n):
    if n > 0:
        l = list(map(int, str(n)))
        return sum(l)
print(digit_sum(45))
print(digit_sum(4))
print(digit_sum(-3))

def digit_sum_recursive(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + digit_sum_recursive(n//10)
    return n


print(digit_sum_recursive(45))

print(list(range(10)))
