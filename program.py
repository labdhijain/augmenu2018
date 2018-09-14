#!/usr/bin/env python2


choice='''
press 1 to check MAC Address
press 2 to total amount to RAM and CPU
press 3 to your cuurent OS type and OS name
press 4 to check  your current internet connection:
press 5 to  close your internet connection
press 6 to check your current date and time:
press 7 to check logout:
press 8 to turn off everyone's internet in your current network:
'''

print choice



choice = raw_input()

if choice == '1' :
        execfile('k1.py')

if choice == '2' :
        execfile('k2.py')

if choice == '3' :
        execfile('k3.py')

if choice == '4' :
        execfile('k4.py')

if choice == '6' :
        execfile('k6.py')


if choice == '7' :
        execfile('k7.py')



else:
        print "no rang"


