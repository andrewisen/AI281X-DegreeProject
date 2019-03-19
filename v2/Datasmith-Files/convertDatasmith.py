#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from itertools import takewhile


def readLines():
	file = "data.udatasmith"
	
	try:
		fileObject = open(file)
	except Exception as e:
		print("Error: File not loaded")
		return

	lines = fileObject.read().splitlines()
	#lines = fileObject.read()
	
	fileObject.close()

	return lines

def removeData(lines):
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
	return lines

def convert(lines):
	
	for line in lines:
		removeSpace = line.split(" ")
		removeSpace = "".join(removeSpace)
		#removeTab = removeSpace.split("\t")
		#removeTab = "".join(removeTab)
		print(removeTab)

	return 



def build_tree(lines):
	is_tab = '\t'.__eq__


	lines = iter(lines)
	stack = []
	for line in lines:
		indent = len(list(takewhile(is_tab, line)))
		stack[indent:] = [line.lstrip()]
	
	#for _ in stack:
	#	print(_)


def main():
	lines = readLines()
	lines = removeData(lines)
	
	lines = "".join(lines)
	#print(lines,end="")

	#convert(lines)
	build_tree(lines.split('\n'))


if __name__== "__main__":
	main()