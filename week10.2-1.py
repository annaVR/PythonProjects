__author__ = 'anna'
file=raw_input("Enter file: ")
fh=open(file)
hours={}
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        line=line.split()
        time=line[5]
        time=time.split(':')
        hour=time[0]
        hours[hour]=hours.get(hour,0)+1
sorted([(v,k) for k,v in hours.items()])