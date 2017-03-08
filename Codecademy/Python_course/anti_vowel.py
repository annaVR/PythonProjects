__author__ = 'anna'
def anti_vowel(text):
    text = str(text)
    vowels = 'aeiouAEIOU'
    new_string = ''
    for letter in text:
        if vowels.find(letter) == -1:
            new_string += letter
    return new_string

print(anti_vowel('anna'))