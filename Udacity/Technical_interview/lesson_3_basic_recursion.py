__author__ = 'anna'
def recursion(inp):
    if inp <= 0:
        return inp
    else:
        print(inp)
        output = recursion(inp - 1)
        print(output)
        return output

print(recursion(-10))
print()
print(recursion(15))


