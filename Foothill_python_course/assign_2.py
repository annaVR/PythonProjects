__author__ = 'anna'

#name of student - Anna Romanovskaia
#the program prints the form letters asking for votes in the upcoming election.

#empty list
data = []

# for loop creates a list of tuples.
for round in range(3):
    #getting user input and assigning it to variables
    addressee = input("Enter the addressee's name: ")
    candidate = input("Enter the candidate's first/lastname: ")
    sender = input("Enter the sender's name: ")
    #creating tuple from variables
    tup = (addressee, candidate, sender)
    #appending tuple to list
    data.append(tup)

#printing form letters using for loop and string formatting ("%s" % value to replace %s)
for item in data:
    print(
"""
Dear %s,

I would like you to vote for %s

because I think he is best for this state.

Sincerely,

%s.
""" % (item[0], item[1], item[2]))
    print()

#run of the program in Pycharm:
# /usr/local/Cellar/python3/3.5.1/bin/python3 /Users/anna/PycharmProjects/PythonProjects/Foothill_python_course/assign_2.py
# Enter the addressee's name: William
# Enter the candidate's first/lastname: Arnold Schwarzenegger
# Enter the sender's name: Anna
# Enter the addressee's name: Margot
# Enter the candidate's first/lastname: Edmund Brown
# Enter the sender's name: Jerry
# Enter the addressee's name: Thomas
# Enter the candidate's first/lastname: Gray Davis
# Enter the sender's name: Inga
#
# Dear William,
#
# I would like you to vote for Arnold Schwarzenegger
#
# because I think he is best for this state.
#
# Sincerely,
#
# Anna.
#
#
#
# Dear Margot,
#
# I would like you to vote for Edmund Brown
#
# because I think he is best for this state.
#
# Sincerely,
#
# Jerry.
#
#
#
# Dear Thomas,
#
# I would like you to vote for Gray Davis
#
# because I think he is best for this state.
#
# Sincerely,
#
# Inga.
#
#
#
# Process finished with exit code 0

