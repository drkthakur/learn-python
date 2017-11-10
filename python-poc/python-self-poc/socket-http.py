import socket
import time
mysoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysoc.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysoc.send(cmd)


while True:
    data = mysoc.recv(512)
    if (len(data) < 1):
        break
    # print(data.decode())
mysoc.close()


import urllib.request
fhand = urllib.request.urlopen('http://www.sample-videos.com/text/Sample-text-file-10kb.txt')
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)