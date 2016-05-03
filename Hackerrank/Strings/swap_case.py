__author__ = 'anna'
st = input()
st_sw = st.swapcase()
print(st_sw)
#same:
print (''.join([i.lower() if i.isupper() else i.upper() for i in st]))

