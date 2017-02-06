#the prigram counts unique words in a file

def clean(string):
    result = ''
    for letter in string:
        if letter.isalpha():
            result += letter
    return result.lower()

def main():
    unique_words = set()

    filename = input("Enter filename(default: she_will_be_loved.txt): ")
    if len(filename) == 0:
        filename = 'she_will_be_loved.txt'
    fhandle = open(filename, 'r')

    for line in fhandle:
        words = line.split()
        for word in words:
            cleaned = clean(word)
            if len(cleaned) > 0:
                unique_words.add(cleaned)
    print('The document contains', len(unique_words))
    print(unique_words)
    print(sorted(unique_words))

main()