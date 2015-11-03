__author__ = 'anna'
#fortune cookie simulator
import random
print "Welcome to the fortune cookie sumulator!"
print "If you want to finish the game, press \"q\"."
inp=int
while True:
    fortune_num=random.randrange(0,5)
    inp=raw_input("Press any key to generate a number: ")
    if inp=="q": break
    print "You fortune number is", fortune_num,"."

print "Bye!"