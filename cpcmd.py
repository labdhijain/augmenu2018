#!/usr/bin/python

import os.path
from os import path 
import sys
import pathlib

src_file=sys.argv[0]
dst_file=sys.argv[2:]

if sys.argv[2]==("-v"):
	
	dst_file=sys.argv[3:]
	#check if file exists
	file=pathlib.Path(src_file)
	if file.exists():
		
		#check if src is a file
		path=src_file
		if os.path.isfile(path):

			#opening source file
			f=open(src_file,"r")
			src_data=f.read()
			f.close()

			#copying into destination file
			for i in dst_file:
				f1=open(i,"w")
				f1.write(src_data)
				f1.close()
				print(src_file + "----->" + i)
		else:
			print("Source File is not a file..!")

	else:
		print ("File does not exist..!")

else:
	#check if file exists
	file=pathlib.Path(src_file)
	if file.exists():
		
		#check if src is a file
		path=src_file
		if os.path.isfile(path):

			#opening source file
			f=open(src_file,"r")
			src_data=f.read()
			f.close()

			#copying into destination file
			for i in dst_file:
				f1=open(i,"w")
				f1.write(src_data)
				f1.close()
		else:
			print("Source File is not a file..!")

	else:
		print ("File does not exist..!")

