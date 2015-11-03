__author__ = 'anna'
#counting programm

print "Welcome to the counting game!"
start=int(raw_input("Enter a starting point: "))
end=int(raw_input("Enter an ending point: "))
augment=int(raw_input("Enter an augment: "))
for i in range(start,(end+1),augment):
    print i
raw_input("Enter any key to exit")