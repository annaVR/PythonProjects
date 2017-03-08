__author__ = 'anna'



def filter_files(oldfile, newfile):
    o = open(oldfile, 'r')
    n = open(newfile, 'w+')
    for line in o: # for line in o.readlines(): - the diff is that readlines store the entire content in memory
        if line[0] == '\n':
            continue
        if line[0] == '#':
            continue
        n.write(line)
    n.seek(0, 0)
    filtered = n.read()
    o.close()
    n.close()
    return filtered

print(filter_files('/Users/anna/Documents/food.txt', '/Users/anna/Documents/new_file.txt'))

