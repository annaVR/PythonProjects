__author__ = 'anna'

arr = [int(x) for x in input('Enter array:').split()]
odds = []


# for item in arr:
#     if item % 2 != 0:
#         odds.append(item)
odds = [x for x in arr if x % 2 != 0]

print(sorted(odds, reverse=True))
