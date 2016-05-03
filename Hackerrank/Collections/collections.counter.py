__author__ = 'anna'
from collections import Counter
#num_shoes = int(input())
num_shoes = 10
#shoe_counter = Counter(map(int, input().split()))
list_of_shoes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
shoe_counter = Counter(map(int, list_of_shoes))
#n_custom = int(input())
n_custom = 6
money = 0
size_price = [(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)]

# for i in range(n_custom):
#     size, price = map(int, input().split())
#     if shoe_counter[size] > 0:
#         shoe_counter[size] -= 1
#         money += price
# print(money)



