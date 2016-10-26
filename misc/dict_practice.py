__author__ = 'anna'

import urllib
import string

st = urllib.urlopen('http://py4inf.com/code/romeo.txt').read()

print st

words = st.split()
print words

d = {}

for word in words:
    d[word] = d.get(word, 0) + 1
print d

d_2 = {}

for letter in 'But soft what light through yonder window breaks':
    d_2[letter] = d_2.get(letter, 0) + 1
print '# 2'
print d_2

d_3 = {}
for letter in 'But soft what light through yonder window breaks':
    if letter == 'a':
        d_3[letter] = d_3.get(letter, 0) + 1
print '#3'
print d_3


d_4 = {}
for letter in string.ascii_lowercase:
    for letter_2 in 'But soft what light through yonder window breaks':
        if letter == letter_2:
            d_4[letter] = d_4.get(letter, 0) + 1
        elif not letter in d_4:
            d_4[letter] = 0
print '#4'
print d_4