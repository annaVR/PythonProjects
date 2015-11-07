__author__ = 'anna'
def delete_content(f_name):
    with open(f_name,"wb"):
        pass


import pickle

try:
    f=open("pickles.dat","rb")
    high_scores=pickle.load(f)
    print (high_scores)
    f.close()
except:
    print ("Empty!")



delete_content("pickles.dat")

try:
    f=open("pickles.dat","rb")
    high_scores=pickle.load(f)
    print (high_scores)
    f.close()
except:
    print ("Empty!")
