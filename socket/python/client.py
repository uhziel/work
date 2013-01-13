#!/usr/bin/env python2
# via http://docs.python.org/2/library/socket.html
# via http://docs.python.org/2/howto/sockets.html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(("localhost", 2013))
except socket.error as msg:
    print("cannot connect localhost:2013")
    s.close()
    exit(1)
msg = s.recv(2000)
print(msg)
