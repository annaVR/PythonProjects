__author__ = 'anna'
#jumble game with hints and rewards

print "Welcome to the Jumble game! The computer randomly choose a word from a list. Then make a jumble from it\
      and present it to the user. The user has to guess a word. If the user is stuck he can have a hint, but no rewards\
 in such case."
print "If you want to finish the game, print \"Enter\" at the prompt."
import random
WORDS=("cat","apple","mirror")
word=random.choice(WORDS)
position=WORDS.index(word)

correct=WORDS[position]
HINTS=("It is an animal.","It is a fruit.","It is made of glass.")
hint=HINTS[position]
reward=""
jumble=""
while word:
    index=random.randrange(len(word))
    jumble+=word[index]
    word=word[:index]+word[index+1:]
print "\nJUMBLE WORD IS: ",jumble
guess=raw_input("Enter your guess: ")
while guess !=correct and guess!="":
    print "Sorry, it is not it."
    answer=raw_input("Do you want a hint? Enter \"yes\" or \"no\": ")
    while answer.lower()!="yes" and answer.lower()!="no":
        answer=raw_input("The answer is incorrect. Do you want a hint? Enter \"yes\" or \"no\": ")
        print "Answer", answer
    if answer.lower()=="yes":
        print hint
        reward=0
        guess=raw_input("Enter your guess: ")
        answer=""
        print "Answer is ", answer
        if guess=="":break
        else:continue
    elif answer.lower()=="no":
        reward=1
        guess=raw_input("It is ok if you do not want a hint. Enter your guess: ")
        answer=""
        print "Answer is ", answer
        if guess=="":break
        else:continue
if guess==correct:
    print "Congratulation, you guessed it right!"
    if reward==0:
        print "Sorry, you have no rewards because you've used a hint."
    else:
        print "You have a reward because you didn't use a hint!"

raw_input("Press any key to exit: ")







