
__author__ = 'anna'
print "Welcome to the counting backward game!"
print "If you want to finish the game, press \"Enter\" at prompt."
backward=""

phrase=raw_input("Enter your phrase: ")

while phrase:
    index=-1
    print index
    backward+=phrase[index]
    print backward
    phrase=phrase[0:(len(phrase)-1)]
    print phrase
    if phrase =="":
        phrase=raw_input("Enter your phrase: ")
        backward=""



raw_input("Press any key to exit.")
