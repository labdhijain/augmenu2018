#!/usr/bin/env python2

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.122.1"
port=7089

while 4 > 2 :
	msg=raw_input("enter message")
	s.sendto(msg,(ip,port))
