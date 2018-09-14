#!/usr/bin/env python2

import socket
import time
import matplotlib.pyplot as plt 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.10.183"
port=7089

s.bind((ip,port))
	

#receiving data from target machine
v=s.recvfrom(100)
a=v[0]
print("message is:",a)

time.sleep(2)

#python program to count number of words in dict.
def word_count(str):
	counts = dict()
	words =str.split()
	
	for word in words:
		if word in counts:
			counts[word] +=1
		else :
			counts[word] = 1
	return counts
print( word_count(a))

time.sleep(2)
#plotting graph out of dict
#use ticks as x list is of string type

xticks = list(word_count(a).keys())
print(xticks)

time.sleep(2)

y = list(word_count(a).values())
print(y)
time.sleep(2)
x =range(len(xticks))

#ticks used in plot 
plt.xticks(x,xticks)
#labelling



plt.xlabel("name of people")
plt.ylabel("number of occurance")
plt.scatter(x,y,label="general word count with dots ",marker="*",s=200)
plt.plot(x,y,label="general word count with line")
plt.bar(x,y,label="bar plot")
#plt.plot(x1,y1,label="fake data")
plt.legend()
plt.grid()
plt.show()


plt.title("First Graph")
                      
