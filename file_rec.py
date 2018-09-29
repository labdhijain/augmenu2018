#!/usr/bin/python

import socket,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="127.0.0.1"
port1=7890
port2=8888

s.bind(("",port2))

user=s.recvfrom(20)
password=s.recvfrom(20)
print (user[0])
print (password[0])

if ("root") in user and ("123") in password:
	msg1=("Correct")
	s.sendto(msg1,(ip,port1))
	print ("OK")
	while True:
		data=s.recvfrom(20)
		file_name=s.recvfrom(20)	
		data1=data[0]
		file_name1=file_name[0]
		name1=("copy_" + file_name1)

		new_data=open(name1,'w')
		new_data.write(data1)
		new_data.close()
		
else:
	msg=("wrong")
	s.sendto(msg,(ip,port1))
	print ("INVALID PASSWORD OR USERNAME..!!")
exit()
