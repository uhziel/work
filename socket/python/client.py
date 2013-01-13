#!/usr/bin/env python2
# via http://docs.python.org/2/library/socket.html
# via http://docs.python.org/2/howto/sockets.html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 2013))
msg = s.recv(2000)
print(msg)
