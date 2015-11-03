__author__ = 'anna'
#Character creator program
#pool of 30 points
#strenght
#health
#wisdom
#dexterity
#the player should be able to spend points from the pool on any attribute and should also be able to take points from
#an attribute and put them back into the pool
print "Welcome to the character creator game!\
you have a pool of 30 points to spend of 4 attributes: strenght,health,wisdom and dexterity.\
Your choices:\n 0-quit" \
      "\n 1-spend some points on attribute\n" \
      " 2-take points back to the pool"
attributes={"strenght":0,
            "health":0,
            "wisdom":0,
            "dexterity":0}

pool_so_far=30

choice=None
while choice!=0:
    choice=int(raw_input("Your choices:\n 0-quit" \
      "\n 1-spend some points on attribute\n" \
      " 2-take points back to the pool.\n Enter your choice:"))

    if choice==1 and pool_so_far==0:
        print "Your pool is empty. You cannot buy any attributes."

    elif choice==1:

        input=raw_input("Which attribute do you want to buy:")
        key=input.lower()

        while key not in attributes:
            print "There is no such attribute in a list."
            input=raw_input("What kind of attribute do you want to buy:")
            key=input.lower()
            print "Key",key

        value=int(raw_input("How much points do you want to spend on this attribute:"))
        print "Value", value
        while pool_so_far-value<0:
            print "You attempt to spend to much points from your pool."
            print "Pool_so_far",pool_so_far
            value=int(raw_input("How much points do you want to spend on this attribute:"))
            print "Value", value



        attributes[key]= attributes[key]+value
        print attributes
        pool_so_far-=value
        print "pool_so_far",pool_so_far



    elif choice==2:
        input=raw_input("From wich attribute do you want to take points:")
        key=input.lower()
        if attributes[key]==0:
            print "You cannot take points from this attribute because you have 0 point on it."
            continue
        while key not in attributes:
            print "There is no such attribute in a list."
            input=raw_input("From wich attribute do you want to take points:")
            key=input.lower()
            print "Key",key

        value=int(raw_input("How much points do you want to take from this attribute:"))

        print "Value",value
        while attributes[key]-value<0:
            print "You attempt to take out too much points."
            print "You have", attributes[key]," points on this attribute."
            value=int(raw_input("How much points do you want to take from this attribute:"))
            print "Value",value


        attributes[key]=attributes[key]-value
        pool_so_far+=value
        print attributes
        print "Pool so far",pool_so_far



if choice==0:
    print "Good bye!"
raw_input("\nPress the enter key to exit.")