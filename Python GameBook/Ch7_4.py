__author__ = 'anna'


# Trivia challenge game_4

import sys

def open_file(file_name,mode):
    try:
        the_file=open(file_name,mode)
    except IOError as e:
        print("Unable to open the file. Ending the program", e)
        input("Press any key to exit")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line=the_file.readline()
    line=line.replace("/","\n")
    return line

def ask_name(question):
    name=input(question)
    return name

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
    print("Welcome to the Trivia Challenge game!\n")
    print(title)




def main():
    trivia_file=open_file("trivia_2.txt","r")
    title=next_line(trivia_file)
    welcome(title)

    score=0

    category,question,answers,correct,explanation,point_value=next_block(trivia_file)
    while category:
        print(category)
        print(question)
        print("Answers:")
        for i in range(4):
            print(i+1,"---",answers[i])

        answer=input("Enter your answer:")
        if answer==correct:
            print("Congratulation! Your answer is right.")
            point_value=int(point_value)
            score+=point_value
            print("Your score is", score)
        else:
            print("Sorry. Your answer is wrong.")
            print(explanation)
        category,question,answers,correct,explanation,point_value=next_block(trivia_file)

    trivia_file.close()


    name=ask_name("We will record your score. Please, enter your name:")




    try:
        f_1=open("write_scores.txt","r")

        high_scores=f_1.readlines()


        f_1.close()
        print("High scores previous:",high_scores)
        high_score=name+" "+str(score)+"\n"

        high_scores.append(high_score)


        print("New High scores:",high_scores)
    except:
        high_scores=[]
        high_score=name+" "+str(score)+"\n"

        high_scores.append(high_score)
        print("High scores:",high_scores)

        pass


    f=open_file("write_scores.txt","w")


    f.writelines(high_scores)

    f.close()

    print("\n\nGame over!\nYour total score is:", score)
    print("High scores:")
    for i in high_scores:
        i=i.replace("\n","")
        print(i)



main()
input("Press enter key to exit.\n")

