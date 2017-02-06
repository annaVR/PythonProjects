__author__ = 'anna'


def digit_sum(n):
    if n ==0: return 0
    print(digit_sum(n//10) + n % 10)
    return digit_sum(n//10) + n % 10

print(digit_sum(1457))
