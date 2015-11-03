__author__ = 'anna'
#Guess my number (limited number of times)
#The computer pick the number between 1 and 100
#The player tries to gess it and the computer lets the player know it the guess is too high, too low or just right
#The player has 10 attempts only.

import random
print "Welcome to the Guess my number game!"
print "I'm thinking of a number between 1 and 100."
print "Try to guess it in as few attempts as possible. The maximum number of attempts is 10."\
+ "If you exceed 10 times, you loose the game."
number=random.randint(1,100)
print number
guess=int(raw_input("Guess a number: "))
tries=0
for i in range(0,10):
    tries+=1
    if guess==number:
        print "Congratulation! You guessed it right in", tries, "tries!"
        break
    elif tries==10:
        print ("The number of allowed attempt is 10, so it was your last one. You loose the game, sorry.")
        break
    elif guess>number:
        print "It is to high!\nTry again!"
        guess=int(raw_input("Guess a number: "))
    elif guess<number:
        print "It is too low!\nTry again."
        guess=int(raw_input("Guess a number: "))


raw_input("\nPress any key to exit.")

