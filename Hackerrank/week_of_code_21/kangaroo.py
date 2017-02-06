__author__ = 'anna'

start1, rate1, start2, rate2 = 0, 3, 4, 2


landing1 = start1
landing2 = start2
def if_they_meet(jump1, jump2, rate1, rate2):
    #jump1, jump2 = jump1, jump2
    #rate
    while jump1 or jump2:
        jump1 += rate1
        jump2 += rate2
        if jump1 == jump2:
            return(jump1, "YES")
    return("NO")
print(if_they_meet(landing1, landing2, rate1, rate2))
