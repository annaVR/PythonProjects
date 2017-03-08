__author__ = 'anna'

import urllib.request

url = 'http://openbookproject.net/thinkcs/python/english3e/files.html'
file = '/Users/anna/Documents/url_file.txt'

urllib.request.urlretrieve(url, file)

# save content of url to a string

def retrieve_page(url):
    socket = urllib.request.urlopen(url)
    data = str(socket.read())
    status = socket.status
    socket.close()
    return status, data

for item in retrieve_page(url):
    print(item)

