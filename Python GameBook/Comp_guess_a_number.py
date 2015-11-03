__author__ = 'anna'
#Ch3_guess a number
#The player picks a number between 1 and 25
#The computer has to guess the number

import random
print "Hello! Welcome to the game!"
number=int(raw_input ("Please, pick a number between 1 and 25 that computer has to guess: "))
tries=1
l_guess=0
h_guess=26
guess=random.randint(l_guess,h_guess)
print guess
while guess!=number:
    if guess>number:
        tries+=1
        h_guess=guess
        guess=random.randint(l_guess,h_guess)
        print l_guess, h_guess
        print guess
    else:
        tries+=1
        l_guess=guess
        guess=random.randint(l_guess,h_guess)
        print l_guess, h_guess
        print guess
print "Congratulation, Computer! The number is", number, ". You guessed it in", tries, "tries."
