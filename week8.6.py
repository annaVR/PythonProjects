numbers=list()
while True:
    entry = raw_input ("Enter a number: ")
    if entry == "done": break
    value = float(entry)
    numbers.append(value)
print "Maximum: ", max(numbers)
print "Minimum: ", min(numbers)
