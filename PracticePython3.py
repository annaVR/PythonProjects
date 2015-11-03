__author__ = 'anna'
nums=[1,1,2,3,5,8,13,21,34,55,89]
print "The list of numbers is: ", nums
user_num=int(raw_input("Enter your number: "))
sm3_nums=list()
sm_nums=list()
for num in nums:
    if num<5:
        sm3_nums.append(num)
print "Numbers less than 5 from the original list are:",sm3_nums
for num in nums:
    if num<user_num:
        sm_nums.append(num)
        print sm_nums
print "Numbers less than your number are:",
for item in sm_nums:
    print item
#same:
# count=0
# for item in sm_nums:
#     print sm_nums[count]
#     count=count+1
