__author__ = 'anna'
# Trivia challenge game

import sys

def open_file(file_name,mode):
    try:
        the_file=open(file_name,mode)
    except IOError as e:
        print ("Unable to open the file. Ending the program", e)
        input ("Press any key to exit")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line=the_file.readline()
    line=line.replace("/","\n")
    return line

def next_block(the_file):
    category=next_line(the_file)
    question=next_line(the_file)
    answers=[]
    for i in range(4):
        answers.append(next_line(the_file))
    correct=next_line(the_file)
    if correct:
        correct=correct[0]

    explanation=next_line(the_file)
    point_value=next_line(the_file)

    return category,question,answers,correct,explanation,point_value

def welcome(title):
    print ("Welcome to the Trivia Challenge game!\n")
    print (title)

def main():
    trivia_file=open_file("trivia_1.txt","r")
    title=next_line(trivia_file)
    welcome(title)
    score=0

    category,question,answers,correct,explanation,point_value=next_block(trivia_file)
    while category:
        print (category)
        print (question)
        print ("Answers:")
        for i in range(4):
            print (i+1,"---",answers[i])

        answer=input("Enter your answer:")
        if answer==correct:
            print("Congratulation! Your answer is right.")
            point_value=int(point_value)
            score+=point_value
            print ("Your score is", score)
        else:
            print ("Sorry. Your answer is wrong.")
            print (explanation)
        category,question,answers,correct,explanation,point_value=next_block(trivia_file)

    trivia_file.close()

    print ("\n\nGame over!\nYour total score is:", score)

main()
input("Press enter key to exit.\n")

