# user input
s = input()

# uses all 5 methods on each character and creates a list for each,
# containing the results of each method used on the character.
newList = [[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]

# rotates lists clockwise to get lists of each method instead
print(zip(*newList))
rotated = list(zip(*newList))
print(rotated)


# prints whether or not a True is present for each List
print("\n".join([str(i) for i in (any(i) for i in rotated)]))