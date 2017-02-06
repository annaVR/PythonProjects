__author__ = 'anna'
import timeit

def fibonacci(length):
    l = [0, 1]

    if length >= 2:
        for _ in range(length-2):
            last = l.pop()
            before_last = l.pop()
            num = before_last + last
            l.extend([before_last, last, num])
    else:
        l = l[:length]
    print(list(map(lambda x: x**3, l)))
def main():
    n = 1
    fibonacci(n)
print(timeit.timeit(main, number=1))

def fibonacci_2(length):
    a = [0, 1]
    for i in range(2, length):
        a.append(a[i-1] + a[i-2])
    print(list(map(lambda x: x*x*x, a))[:length])

def main_2():
    n = 1
    fibonacci_2(n)

print(timeit.timeit(main_2, number=1))


