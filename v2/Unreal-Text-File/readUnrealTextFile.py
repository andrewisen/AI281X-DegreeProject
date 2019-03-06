#!/usr/bin/env python
# -*- coding: utf-8 -*-

def readLines():
	# NB. Be aware of realtive or absolute path
	file = "data.t3d" 
	
	try:
		fileObject = open(file,encoding='utf-16')
	except:
		print("Error: File not loaded")
		return

	lines = fileObject.read().splitlines()
	fileObject.close()

	return lines

def getObjects(lines):
	beginObjectPhrase = "Begin Object"
	endObjectPhrase = "End Object"

	status = ""
	objects = []
	currentObject = []

	for line in lines:
		if beginObjectPhrase in line: 
			status = "begin"
			pass
		elif endObjectPhrase in line: 
			status = "end"
			objects.append(currentObject)
			currentObject = []
			pass
		else:
			if status == "end":
				continue
			else:
				pass
		
		currentObject.append(line)

	for i in objects:
		print(i)

def main():
	lines = readLines()
	getObjects(lines)

if __name__== "__main__":
	main()