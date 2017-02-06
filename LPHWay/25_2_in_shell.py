def break_words(stuff):
    words = stuff.split(' ')
    return words

def print_last_word(words):
    word = words.pop(-1)
    print(word)