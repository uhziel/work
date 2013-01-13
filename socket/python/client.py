#!/usr/bin/env python2

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 2013))
msg = s.recv(2000)
print(msg)
