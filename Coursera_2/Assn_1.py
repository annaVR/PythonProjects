__author__ = 'anna'

import re

f=open("Assn_1.txt")

nums_total=[]
for line in f:
    line=line.rstrip()
    nums=re.findall("[0-9]+",line)
    if len(nums)>0:
        for i in nums:
            i=int(i)
            nums_total.append(i)
summ=sum(nums_total)
print "Sum:", summ

