__author__ = 'anna'
import re
l = ['1.414','+-1.5486468', '.+0', '1+1.0', 'O.O1']
for i in range(len(l)):
    st = l[i]
    print(bool(re.match(r'^[\+-\-]?\d*\.\d+$', st)))

# True
# False
# False
# False
# False