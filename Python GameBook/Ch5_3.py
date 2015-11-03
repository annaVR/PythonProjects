__author__ = 'anna'
#Who's your Daddy game.

print "\nWelcome to the \"Who\'s your Daddy\" game.\n\
You choices:"
print "0-exit a game\n"\
"1-add a new son-father pair\n" \
"2-replace an existing son-father pair\n" \
"3-delete an existing son-father pair"

import random
pairs={}
choice=None
fathers=["adam","justin","jonathan","silvester","mickey","david","michael"]

while choice!=0:
    choice=int(raw_input("Enter your choice:"))
    if choice ==1:
        son=raw_input("Enter a male\'s name:")
        son=son.lower()
        father=random.choice(fathers)

        print "Father",father

        pairs[son]=father
        print pairs
    elif choice==2:
        print "You have the following son-father pairs:"
        for pair in pairs:
            print pair,pairs[pair]
        son=raw_input("Enter a name of a son which pair you want to replace: ")
        son=son.lower()
        while son not in pairs:
            print ("This son's name is not in son-father pairs.")
            son=raw_input("Enter a name of a son which father you want to replace: ")
        new_father=random.choice(fathers)
        pairs[son]=new_father
        print pairs
    elif choice==3:
        print "You have the following son-father pairs:",pairs
        son=raw_input("Enter a name of a son which pair you want to delete: ")
        son=son.lower()
        while son not in pairs:
            print ("This son's name is not in son-father pairs.")
            son=raw_input("Enter a name of a son which pair you want to delete: ")
            son=son.lower()
        del pairs[son]
        print pairs

if choice==0:
    print "Good buy!"
raw_input("\n\nPress the enter key to exit.")