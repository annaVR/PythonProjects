__author__ = 'anna'
#st, sub_st = input(), input()
st = "ABCDCDC  "
sub_st = "CDC "


ls_sub = list(sub_st.strip())
ls = list(st.strip())
def my_f(x, start):
    return x[start:(start+len(ls_sub))]
start = 0
occ = 0
print(ls)
while True:
    if start == 0:
        start = st.find(sub_st.strip())
    slic = my_f(ls, start)
    print(slic)
    if slic == ls_sub:
        occ+= 1
    if len(slic)< len(ls_sub): break
    start+= 1
print(occ)
