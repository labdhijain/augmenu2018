#!/usr/bin/python2
import socket,commands
# we are looking for udp (user datagram protocol)
#                     IP VERSION IP4    UDP	
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip nand port number
ip = "192.168.10.198"
port=7890

#defining list
timer=[]
while True:
	cmd=raw_input("enter the command:")
	s.sendto(cmd,(ip,port))
	if 'exit' in cmd or 'close' in cmd:
		print "closing server..."
		exit()
	else:
		timer.append(cmd)
		print len(timer)
		if len(timer) > 5:
			print commands.getoutput('clear')
			print timer
			for i in range(len(timer)):
				timer.pop()
		else :
			pass 


s.close()


