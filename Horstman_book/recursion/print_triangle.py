def print_triangle(side_length):
    if side_length < 1:
        return
    print_triangle(side_length - 1)
    print('*' * side_length)

def print_reverse_triangle(side_length):
    if side_length < 1:
        return
    print('*' * side_length)
    print_reverse_triangle(side_length - 1)

def print_another_triangle(side_length, total):
    if side_length < 1:
        return
    print_another_triangle(side_length - 1, total)
    empty = total - side_length
    stars = total - empty
    print(' ' * empty + '*' * stars)
    # empty = side_length - 1
    # stars = side_length - empty
    # print(' ' * empty + '*' * stars)

print_triangle(5)
print()
print_reverse_triangle(5)
print()

print_another_triangle(5, 5)
