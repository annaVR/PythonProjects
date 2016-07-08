__author__ = 'anna'

def reverse(text):
    if isinstance(text, str):
        j = [text[i] for i in reversed(range(len(text)))]
        print(j)
        print(''.join(j))

def reverse_2(text):
    l = list(text)
    j = [l.pop() for i in range(len(text))]
    print(''.join(j))

def reverse_3(text):
    l = list(range(1, len(text) +1))
    length = len(text)
    new_string = ''
    for i in l:
        new_string += text[length - i]
        print(new_string)
    print(new_string)

reverse('baba')
reverse_2('vava')
reverse_3('nana')

