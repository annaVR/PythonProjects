def print_triangle(side_lenght):
    if side_lenght < 1: return
    print_triangle(side_lenght - 1)
    print("*" * side_lenght)

def print_rev_triangle(side_lenght):
    if side_lenght < 1: return
    print("[]" * side_lenght)
    print_rev_triangle(side_lenght - 1)

print_triangle(4)

print_rev_triangle(4)
