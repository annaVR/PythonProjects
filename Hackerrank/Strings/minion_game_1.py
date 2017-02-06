__author__ = 'anna'

vowels = 'AEIOU'
conson = 'BCDFGHJKLMNPQRSTVWXYZ'

st = input()

kevin = 0
stuart = 0
for i in range(len(st)):
    if st[i] in vowels:
        print(st[i])
        kevin += len(st) - i

for j in range(len(st)):
    if st[j] in conson:
        print(st[j])
        stuart += len(st) - j

if kevin > stuart:
    print('Kevin {}'.format(kevin))
elif stuart > kevin:
    print('Stuart {}'.format(stuart))
else:
    print('Draw')
