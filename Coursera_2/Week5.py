__author__ = 'anna'

import urllib
import xml.etree.ElementTree as ET

url=raw_input("Enter a URL:")
xml=urllib.urlopen(url).read()

comments=ET.fromstring(xml)
items=comments.findall('comments/comment')


summ=list()

for item in items:
    item=int(item.find("count").text)
    summ.append(item)

summ=sum(summ)
print "Sum", summ