__author__ = 'anna'
#from collections import defaultdict
# char_counter = defaultdict(int)
#
# for char in "aabbbccde":
#     char_counter[char] += 1
# sort_dict = sorted(char_counter, key=char_counter.get, reverse=True)
# print(char_counter)

from collections import Counter
str_counter = Counter('hhhjjjbbbcccaaa')
print(str_counter)
for k, v in sorted(str_counter.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(k, v)



m_com = str_counter.most_common(3)


# def get_key_0(item):
#     return item[0]
# def get_key_1(item):
#     return item[0]
# def get_key_1(item):
#     return item[1]
# def get_key_0(item):
#     return item[0]
# print(sorted(m_com, key=get_key_1))
# print(sorted(m_com, key=get_key_0))


# for k, v in str_counter.most_common(3):
#     print(k, v)
#
