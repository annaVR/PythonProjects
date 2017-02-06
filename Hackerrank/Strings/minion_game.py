__author__ = 'anna'

# Y is not considered a vovel in this problem
# STUART - CONSONANTS
# KEVIN - VOWELS

vowels = 'AEIOU'
conson = 'BCDFGHJKLMNPQRSTVWXYZ'

#conson = ''.join([i for i in alpha if i not in vowels])

st = input()
# def substring_occur(strin, subst):
#     count = 0
#     start = 0
#     for i in range(len(strin)):
#         if st[i:i + len(subst)] == subst:
#             count += 1
#             start = st.find(subst)
#     return count, start
#
# # def substring_increm(strin):
# #     for i in range(len(strin))
#
#
#
# score = 0
# count = 0
# for j in range(len(vowels)):
#     occ, start = substring_occur(st, vowels[j])
#     print(occ, start)
#
#     if occ > 0:
#         for i in range(len(st[start:])):
#             subs = st[start:i+2]
#             print(subs)
#             for k in range(len(st[start:])):
#                 if st[start + k:start +k + len(subs)] == subs:
#                     count += 1
#             print(count)


def occ_start(strin, subst):
    occ = 0
    start = 0
    for i in range(len(strin)):
        if strin[i:i + len(subst)] == subst:
            occ += 1
            start = strin.find(subst)
    return occ, start

def substring(strin, i):
    substring = strin[:i+1]
    return substring

def new_string(strin,start):
    new_string = strin[start:]
    return new_string

def substring_count(strin, subst):
    count = 0
    for i in range(len(strin)):
        if strin[i:i + len(subst)] == subst:
            count += 1
    return count

def counting(letters):
    count = 0
    for i in range(len(letters)):
        print("letters[i] = {}".format(letters[i]))
        occ, beg = occ_start(st, letters[i])
        print('Occ = {0}, start = {1}'.format(occ, beg))
        if occ > 0:
            new_str = new_string(st, beg)
            print('new string: {}'.format(new_str))
            for j in range(len(new_str)):
                substr = substring(new_str, j)
                print(substr)
                #for k in range(len(new_str)):
                count += substring_count(new_str, substr)
                print(count)
    return count

kevin = counting(vowels)
stuart = counting(conson)

if kevin > stuart:
    print('Kevin {}'.format(kevin))
elif stuart > kevin:
    print('Stuart {}'.format(stuart))
else:
    print('Draw')







