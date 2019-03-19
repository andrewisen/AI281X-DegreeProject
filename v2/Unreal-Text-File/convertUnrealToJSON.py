#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from tabtree import parser

def readLines():
	file = "data_simple.t3d"
	
	try:
		fileObject = open(file,encoding='ascii')
	except Exception as e:
		print("Error: File not loaded")
		return

	lines = fileObject.read().splitlines()
	#lines = fileObject.read()
	
	fileObject.close()
	return lines

def prepare(lines):
	array = []
	for line in lines:
		line = removeSpace(line)
		array.append(line)
		#print(line)
	return array

def convert(lines):
	originalLines = lines
	beginString = "Begin "
	endString = "End "
	beginIndex = 0
	endIndex = 0
	

	statusLookingForObject = "Looking"
	statusAddingObjects = "Adding"

	status = statusLookingForObject
	

	array = []
	#for line in lines:
	#	line = removeSpace(line)
	#	array.append(line)
		#print(line)

	for index in range(len(lines)):
		line = lines[index]

		if (status == statusLookingForObject) and (beginString in line):
			beginIndex = index
			#line = line.split(" ")
			#line = line.pop(0)
			line = line.split(" ")[1]

			line = ''.join(line)
			
			endString += line

			status = statusAddingObjects
			line = '"' + line + '":{'
			lines[index] = line
			#print(endString)
		if (status == statusAddingObjects) and (endString in line):
			status = statusLookingForObject
			line = "},"
			lines[index] = line
			return convert(lines)
		if (status == statusAddingObjects):
			lines[index] = line 
			
		#else:
			#return convert(lines)
		
		#	print("LOST")

	a = originalLines
	b = lines

	if set(a) == set(b):
		#print("DONE")
		return lines
	else:
		return convert(lines)

def removeSpace(line):

	if " " == line[0]:
		line = line[1:]
		return removeSpace(line)
	else:
		return line

def main():
	lines = readLines()
	lines = prepare(lines)
	lines = convert(lines)

	for _ in lines:
		print(_)
if __name__== "__main__":
	main()