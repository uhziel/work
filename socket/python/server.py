#!/usr/bin/env python2

import socket

# create server socket, reuse addr, for accepting connect.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind
s.bind((socket.gethostname(), 2013))
# listen
s.listen(5)

while True:
    # accept socket
    (c, addr) = s.accept()
    c.send("hello\n")
    c.close()
