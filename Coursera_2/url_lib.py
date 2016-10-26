import urllib.request

fhand = urllib.request.urlopen('http://py4inf.com/code/words.txt')

for line in fhand:
    print(line.decode().strip())

fhand_2 = urllib.request.urlopen('http://marinayammd.com/contact.htm')

for line in fhand_2:
    print(line.decode().strip())
