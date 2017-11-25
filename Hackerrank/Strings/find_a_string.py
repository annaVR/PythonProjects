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

print('Second solution:')
def count_substring(string, sub_string):
    string = string.rstrip()
    sub_string = sub_string.rstrip()
    if string.find(sub_string) == -1:
        return 0
    index = string.find(sub_string)
    count = 1
    while len(string) - (index + 1) >= len(sub_string):
        if string[index + 1: index + 1 + len(sub_string)] == sub_string:
            count += 1
        index += 1
    return count
print(count_substring(st, sub_st))