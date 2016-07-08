__author__ = 'anna'

def is_prime(x):
    if x <= 1:
        return False
    count = 0
    for num in range(1, x + 1):
        if x % num == 0:
            count += 1
            print(count)
        if count > 2:
            return False
    else:
        return True

print(is_prime(1))
print(is_prime(4))
