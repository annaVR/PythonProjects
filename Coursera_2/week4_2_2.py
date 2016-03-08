__author__ = 'anna'

import urllib
import json
import ssl


from BeautifulSoup import *

url = raw_input('Enter URL:')

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#html - is 1 string that contains the whole url content
html = urllib.urlopen(url, context=scontext).read()



#soup is parsable HTLM data
soup = BeautifulSoup(html)

# retrieve all the anchor tags
tags = soup('a')
count=int(raw_input("Enter count:"))
position=int(raw_input("Enter a position:"))
position-=1

for round in range(0,count):
    next=tags[position]

    next_url=next.get('href', None)
    print "Next URL:", next_url
    next_html=urllib.urlopen(next_url, context=scontext).read()
    next_soup=BeautifulSoup(next_html)
    tags=next_soup('a')



#for tag in tags:
    #ext_url=urllib.open (, context=scontext).read()
#for round in count:
    #next_url=tags

#https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html

#https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Scott.html
