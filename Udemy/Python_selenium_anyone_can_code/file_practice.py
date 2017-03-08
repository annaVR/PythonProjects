__author__ = 'anna'

text = 'It. is often useful to fetch data from a disk file and turn it into a list of lines. \n ' \
       'Suppose we have a file containing our friends and their email addresses, one per line in ' \
       'the file. But we’d like the lines sorted into alphabetical order. A good plan is to read ,' \
       'everything into a list of lines, then sort the list, and then write the sorted list back to ' \
       'another file:'

with open('/Users/anna/Documents/file.txt', 'w') as file:
    file.write(text)

symbols = [",", ".", "'", ":", "’", "\n"]
with open('/Users/anna/Documents/file.txt', 'r') as file:
    data = file.read().lower()
    for symbol in symbols:
        new_data = data.replace(symbol, '')
        data = new_data
print(data)
list_words = data.split(' ')
print(list_words)
words = {}
for item in list_words:
    count = words.get(item, 0)
    count += 1
    words[item] = count
print(words)
def get_key(item):
    return item[1]
sort_list = sorted(words.items(), key=get_key, reverse=True)
for tup in sort_list:
    print(tup[0], ':', tup[1])

