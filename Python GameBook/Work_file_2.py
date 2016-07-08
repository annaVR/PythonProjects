from operator import itemgetter
l = [{'name': 'Homer', 'age': 39, 'weight': '80'}, {'weight': '30', 'name': 'Bart', 'age': 10}]
l_name_sorted = sorted(l, key=lambda k: k['name'])
print(l_name_sorted)
l_age_sorted = sorted(l, key=lambda k: k['age'])
print(l_age_sorted)
l_weight_sorted = sorted(l, key=lambda k: k['weight'], reverse=True)
print(l_weight_sorted)

l_weight_sorted_2 = sorted(l, key=itemgetter('weight'))
print(l_weight_sorted_2)

table = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]

a = sorted(table, key=itemgetter(2))
b = sorted(table, key=lambda k: k[2])
print(a, b)
get_2_elem = itemgetter(2)
print(get_2_elem(table))
for elem in table:
    print(get_2_elem(elem))
for elem in table:
    print(itemgetter(2)(elem))

