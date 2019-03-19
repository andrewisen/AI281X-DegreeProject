#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast

def readLines():
	file = "data.t3d"
	
	try:
		fileObject = open(file,encoding='utf-16')
	except Exception as e:
		print("Error: File not loaded")
		return

	lines = fileObject.read().splitlines()
	fileObject.close()

	return lines

def main():
	lines = readLines()
	objects = getObjects(lines)
	specificObjects = getSpecificObjects(objects)
	getMetaData(specificObjects)
	getLocation(specificObjects)
	getRotation(specificObjects)
	
	exportData(specificObjects)

if __name__== "__main__":
	main()