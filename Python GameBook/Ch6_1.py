__author__ = 'anna'
#improved ask for a number function
def ask_number_1(question,low,high,step=1):
    response=None
    while response not in range(low,high):
        response=int(raw_input(question))
    response+=step
    return response

number_1=ask_number_1("Pick a number 0:8: ",0,9)
print number_1

number_2=ask_number_1("Please, pick a number 0:11: ",0,12,3)
print number_2