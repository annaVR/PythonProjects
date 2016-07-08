__author__ = 'anna'

# filter a list: print return the list with only even numbers
def purify(l):
    new_list = [l[i] for i in range(len(l)) if l[i] % 2 == 0]
    return new_list

print(purify([1, 2]))

l = [1, 2, 3, 4, 5, 6]
# another way with filter()
print(list(filter(lambda x: x % 2 == 0, l)))