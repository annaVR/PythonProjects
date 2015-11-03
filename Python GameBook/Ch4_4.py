__author__ = 'anna'
#a game where the comp picks a random word and the player has to guess it.
#the comp tells how many letters in the word. the player has 5 chances to ask if a letter is in the word.
#The computer responds only yes/no. Then, the player must guess the word.

print "Welcome to the game! he comp picks a random word and the player has to guess it.\
the comp tells how many letters in the word. the player has 5 chances to ask if a letter is in the word.\
The computer responds only yes/no. Then, the player must guess the word."
import random
WORDS=("walrus","bobcat","coyot","monkey","nutria")
answer="yes"
while answer=="yes":
    word=random.choice(WORDS)
    print word
    print "The word consists from",len(word),"letters."
    for letter in range(0,6):
        letter=raw_input("Enter you letter. The computer will tell you if a letter in the word: ")
        if letter.lower() in word:
            print "The letter is in the word."
        else:
            print "The letter is not in the word."
    guess=raw_input("Now, you have to guess the word. Enter your guess: ")
    if guess==word:
        print "Comgratulation! You guessed it right."
    else:
        print "Sorry. You did not guess it."
    answer=raw_input("Do you want to play again? If yes, enter \"yes\", if not enter \"no\":")

raw_input("Press any key to exit:")

