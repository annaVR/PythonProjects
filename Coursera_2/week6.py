__author__ = 'anna'

import urllib
import json

url=raw_input("Enter url:")
print "Retrieving", url
uh=urllib.urlopen(url)
data=uh.read()
print "Retrieving", len(data),"characters"

#js is parced json and is python dictionary
js=json.loads(data)
jslst=js["comments"]

summ=[]
count=0
for item in jslst:
    com_count=item["count"]
    count+=1
    summ.append(com_count)
summa=sum(summ)
print "Count:", count
print "Sum:", summa
