from socket import socket
from pickle import dumps
from data import Point, Vector, Line

s = socket()

s.bind(('127.0.0.1', 8080))
s.listen(5)
while True:
    try:
        req = s.accept()
    except:
        print(0)
    req[0].send(dumps((Point, Vector, Line)))
