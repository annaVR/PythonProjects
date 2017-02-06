
#Reads a number from the user and prints out the names of each digit

number = int(input ("Please type a number:"))
digitNames = ('zero','one','two','three','four','five','six','seven','eight','nine')
result = []
while number > 0:
    currentDigit = number % 10  # modulus operator gives remainder after integer division
                              # in this case it is the rightmost digit
    result.append(digitNames[currentDigit])
    number = number // 10   # integer division throws away the remainder
result.reverse()
for num in result:
    print(num, end=" ")
print("\n")

# print my birthday
print("My birthday is on %s/%s/%s" % (6, 27, 1980))


