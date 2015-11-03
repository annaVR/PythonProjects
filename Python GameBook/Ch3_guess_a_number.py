__author__ = 'anna'
#Guess my number
#The computer pick the number between 1 and 100
#The player tries to gess it and the computer lets the player know it the guess is too high, too low or just right

import random
print "Welcome to the Guess my number game!"
print "I'm thinking of a number between 1 and 100."
print "Try to guess it in as few attempts as possible."
number=random.randint(1,100)
print number

guess=int
tries=0
while guess!=number:
    guess=int(raw_input("Guess a number: "))
    tries+=1
    if guess>number:
        print "It is to high!\nTry again!"
    elif guess<number:
        print "It is too low!\nTry again."
print "Congratulation! You guessed it right in just", tries, "tries!"
raw_input("\nPress any key to exit.")
