#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from tabtree import parser

def readLines():
	file = "data.t3d"
	
	try:
		fileObject = open(file,encoding='utf-16')
	except Exception as e:
		print("Error: File not loaded")
		return

	lines = fileObject.read().splitlines()
	#lines = fileObject.read()
	
	fileObject.close()

	return lines

def convert(lines):
	beginString = "Begin "
	endString = "End "

	print(lines)
		

def main():
	lines = readLines()
	convert(lines)
if __name__== "__main__":
	main()