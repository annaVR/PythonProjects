__author__ = 'anna'

st = input()
ls = st.split(' ')
print(ls)
cap_ls = [item.capitalize() for item in ls]
print(' '.join(cap_ls))

print(st.title())
