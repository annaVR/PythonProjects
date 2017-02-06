__author__ = 'anna'
import re

s = 'Words, words, words.'
print(re.split('\W+', s))

print(re.split("([^0-9])", "123+456*/"))

print(re.split(r"([\s\?\!\,\;])+", "!Holy moly, feferoni!"))

# '[\d{,3}[\+\-]{1}]{,5}\d{,3}'
"[\d{,3}\+|\-]{,5}[\d{,3}]{1}"