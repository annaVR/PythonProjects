import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
html = urllib.urlopen(url).read()

# 'BeautifulSoup' object
soup = BeautifulSoup(html)

# list of 'a' anchor tags
# each tag is like a dictionary of HTML attributes
tags = soup('a')

for tag in tags:
    print tag.get('href', None)
print '#2'
for tag in tags:
    print tag
