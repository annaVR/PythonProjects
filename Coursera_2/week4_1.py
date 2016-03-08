__author__ = 'anna'
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags=soup('span')
print tags
summ=list()

for tag in tags:
    num=int(tag.contents[0])
    print 'Number:',num
    summ.append(num)

print summ
print 'Sum:', sum(summ)
