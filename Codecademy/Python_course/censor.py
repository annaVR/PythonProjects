__author__ = 'anna'

def censor(text, word):
    if word == '':
        return None
    else:
        index = None
        l = list(text)
        while text[len(text)-1] != "*":
            index = text.find(word)
            if index == -1:
                break
            else:
                l[index: index + len(word)] = '*' * len(word)
                print('l:', l)
                text = ''.join(l)
        return text



print(censor('banana', 'na'))
print(censor('kukushka', 'u'))
print(censor('kisamurysa', 'r'))
print(censor('kisamurysa', ''))
