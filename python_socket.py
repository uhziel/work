#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import struct
import threading 

#TCP_IP = '192.168.199.187'
TCP_IP = '127.0.0.1'
TCP_PORT = 8888

BUFFER_SIZE = 102400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def read_s(s):
	while True:
		data = s.recv(BUFFER_SIZE)
		if data:
			size = struct.unpack("!L", data[0:4])[0] - 4
			print "data.size()", len(data)
			print "received data:", struct.unpack("!"+str(size)+"s", data[4:])

t = threading.Thread(target=read_s, args=(s,))
t.daemon = True
t.start()

while 1:
	send_data = raw_input('> ')
	if send_data == "quit":
		break
	size = 4 + len(send_data)
	print "size:", size
	s.sendall(struct.pack("!i" + str(len(send_data)) + "s", size, send_data))

s.close()
