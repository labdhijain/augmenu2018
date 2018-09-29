#!/usr/bin/python

import time
import webbrowser

#taking input strings from the user
a= input("Enter First Name: ")
b = input("Enter Last Name: ")

#printing the strings
time.sleep(1)
z=(a+" "+ b)
print (a+" "+ b)

#swapping the printed strings
time.sleep(1)
print("Swapping the printed Data.....")
time.sleep(1)
print(b+" "+a)


#performing google search on z
time.sleep(1)
webbrowser.open("https://www.google.com/search?client=ubuntu&channel=fs&q=%s &ie=utf-8&oe=utf-8"%z)

#performing google image search on z
time.sleep(1)
webbrowser.open("https://www.google.com/search?q=%s         &client=ubuntu&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjDja2r7ZvdAhXHb30KHTajDTEQ_AUICigB&biw=1280&bih=406"%z)
