#stones and jewels
S = 'anna'
J = 'gn'

no_duplicate_stone = []
for stone in S:
    if stone not in no_duplicate_stone:
        no_duplicate_stone.append(stone)
print(no_duplicate_stone)

count = 0
for stone in no_duplicate_stone:
    if stone in J:
        count += 1
print(count)

#morse
print('morse:')
morse = [".-","-...","-.-.","-..",".","..-.","--.",
         "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

words = ['gin', 'zen', 'gig', 'msg']

list_morse = [''.join(morse[ord(c)-ord('a')] for c in word) for word in words]
print('list comprehension: {}'.format(list_morse))
print('set from list comprehension: {}'.format(set(list_morse)))

words_in_morse = []
for word in words:
    word_in_morse = [''.join(morse[ord(letter) - ord('a')] for letter in word)]
    words_in_morse.append(*word_in_morse)
print("list common: {}. set: {}".format(words_in_morse, set(words_in_morse)))

seen = {"".join(morse[ord(c) - ord('a')] for c in word) for word in words}
print(seen, len(seen))

#832 flipping an image
image = [[1,1,0],[1,0,1],[0,0,0]]
B = []
for item in image:
    item.reverse()
    print(item)
    for i in range(len(item)):
        if item[i] == 0:
            item[i] = 1
        elif item[i] == 1:
            item[i] = 0
    B.append(item)
print(B)

#905 Sort array by parity
a = [3,1,2,4]
even = []
odd = []
for item in a:
    if item%2 == 0:
        even.append(item)
    else:
        odd.append(item)
print(even, odd)
print(even + odd)
even.extend(odd)
print(even)
