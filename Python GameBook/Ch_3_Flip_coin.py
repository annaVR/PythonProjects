__author__ = 'anna'
#flip a coin 100 times game
#Reports the number of heads and tails.

import random
heads=0
tails=1
h_count=0
t_count=0
for i in range(0,100):
    flip_result=random.randint(0,1)
    if flip_result==0:
        h_count+=1
    else:
        t_count+=1
print "You've flipped the coin 100 times."
print "Heads count is", h_count, "."
print "Tails count is", t_count, "."