__author__ = 'anna'

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

mysock.send('GET http://py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode('utf-8'))

while True:
    bytes = mysock.recv(512)
    text = bytes.decode('utf-8')

    if len(text) < 1:
        break
    print(text)
mysock.close()

mysock_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock_2.connect(('www.py4inf.com', 80))

mysock_2.send('GET http://www.py4inf.com/code/intro-short.txt HTTP/1.0\n\n'.encode('utf-8'))

while True:
    bytes_2 = mysock_2.recv(512)
    text_2 = bytes_2.decode('utf-8')
    if len(text_2) < 1:
        break
    print(text_2)
mysock_2.close()

print(text)
words = text.strip()
print(words)