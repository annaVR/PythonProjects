file = raw_input ('Enter file:')
fhandle=open(file)
names=dict()
count=0
for line in fhandle:
    line=line.rstrip()
    if line.startswith("From "):
        line=line.split()
        n=line[1]
        names[n]=names.get(n,0)+1
for name in names:
    if names[name]>count:
        count=names[name]
        maxname=name
print maxname, count
