__author__ = 'anna'
# n, l = int(input().strip()), list(map(int, input().strip().split()))
# print(all([all(elem > 0 for elem in l), any(list(map(int, str(abs(elem)))) == list(reversed(list(map(int, (str(abs(elem))))))) for elem in l)]))



# n = input();s = map(int, raw_input().split())
s = [12, 9, 61, 5, 14]
print ([False, any(map(lambda x: str(x) == str(x)[::-1], s))][all(map(lambda x: x>0, s))])

print(list(map(lambda x: x + 2, s)))

s_2 = 'lambda'
print(s_2[::-1])

