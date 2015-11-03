__author__ = 'anna'
#A program will print a list of words in a random order. The program should print all the words and not to repeat any.
import random
words=["cat","dog","bird","walrus","pig"]

for item in words:
    word=random.choice(words)
    print word
    index=words.index(word)
    print index
    words=words[:index]+words[index+1:]
    print words
    new_list.append(word)
    print new_list
raw_input("Press any key to exit: ")