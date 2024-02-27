from socket import socket
from pickle import loads

s = socket()

s.connect(('127.0.0.1', 8080))

data = loads(s.recv(2048))
for pack in data:
    print(pack)