#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from tabtree import parser

def readLines():
	file = "data.udatasmith"
	
	try:
		#fileObject = open(file,encoding='utf-16')
		fileObject = open(file)
	except Exception as e:
		print("Error: File not loaded")
		return

	lines = fileObject.read().splitlines()
	#lines = fileObject.read()
	
	fileObject.close()

	return lines

def convert(lines):
	matchingLines = [
		"<Host>",
		"<Application Vendor=",
		"<User ID=",
		"Export Duration",
		]

	for matchingLine in matchingLines:
		for line in lines:
			if matchingLine in line:
				lines.remove(line)		

def main():
	lines = readLines()
	convert(lines)
if __name__== "__main__":
	main()