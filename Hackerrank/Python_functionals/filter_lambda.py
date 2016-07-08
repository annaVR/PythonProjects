__author__ = 'anna'
l_2 = ['dheeraj-234@gmail.com', 'itsallcrap', 'harsh_1234@rediff.in', 'kunal_shin@iop.az', 'matt23@@india.in']

l_1 = ['iu89_in.plus@google.com', 'ill@google.com', 'fill@google1.com']
l = ['learn.point@learningpoint.net', 'learnpoint@learningpoint.net', 'learnpoint@learningpoint.net1']
#['learnpoint@learningpoint.net']
a = []
results = []
for i in range(len(l)):
    if "@" in l[i] and '.' in l[i]:
        first_part = l[i].split('@')
        if len (first_part) == 2:
            user_name, the_rest = first_part
            second_part = the_rest.split('.')
            if len(second_part) == 2:
                website, extension = second_part
                a.append((user_name, website, extension))
print(a)


for j in range(len(a)):
    list_user = list(filter(lambda x: x.isalnum() or x == '_' or x == '-', a[j][0]))
    list_webs = list(filter(lambda x: x.isalnum(), a[j][1]))
    ext = list(filter(lambda x: 0 < len(x) < 4, a[j][2:]))
    print(list_user, list_webs, ext)
    if len(list_user) > 0 and len(list_webs) > 0 and len(ext) > 0:
        if len(a[j][0]) == len(list_user) and len(a[j][1]) == len(list_webs) and len(a[j][2]) == len(ext[0]):
            us = ''.join(list_user)
            wb = ''.join(list_webs)
            st = '@'.join([us, wb])
            print(st)
            email = '.'.join([st, ext[0]])
            print(email)
            results.append(email)
print(list(sorted(results)))



# for j in range(len(a)):
#     user = list(filter(lambda x: x.isalnum() or '_' in x or '-' in x, a[j][:1]))
#     webs = list(filter(lambda x: x.isalnum(), a[j][1:2]))
#     ext = list(filter(lambda x: 0 < len(x) < 4, a[j][2:]))
#     print(user, webs, ext)
#     if len(user) > 0 and len(webs) > 0 and len(ext) > 0:
#         j = '@'.join([user[0], webs[0]])
#         email = '.'.join([j, ext[0]]
#         results.append(email)
# print(results)
# print(sorted(results))

