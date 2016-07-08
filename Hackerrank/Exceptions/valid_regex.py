__author__ = 'anna'
import re
for test in range(int(input().strip())):
    try:
        re.compile(input().strip())
        is_valid = True
    except re.error as e:
        is_valid = False
        print('Error:', e)
    print(is_valid)

#input example: 2, .*\+, .*+