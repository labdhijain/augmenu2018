#!/usr/bin/env python2

import  socket
import  commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#ip="192.168.10.198"
port=7890

s.bind(("",port))

# receive data from client side 
while True :
	client_data = s.recvfrom(20)
#only client data is stored
	recv_cmd=client_data[0]
# executing client data
	if 'exit' in recv_cmd or 'close' in recv_cmd :
		exit()
	else :
		print commands.getoutput(recv_cmd)

s.close()

