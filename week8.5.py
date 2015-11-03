fname=raw_input ("Enter file name: ")
fhandle=open(fname)
count = 0
for line in fhandle:
    line=line.rstrip()
    if line.startswith("From "):
        line=line.split()
        names=line[1]
        print names
        count=count+1
    else:
        continue
print "There were", count, "lines in the file with From as the first word"