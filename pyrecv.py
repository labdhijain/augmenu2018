#!/usr/bin/env python2

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.122.1"
port=7890

s.bind((ip,port))
	

while 5 > 2 :
	print s.recvfrom(100)

                      
