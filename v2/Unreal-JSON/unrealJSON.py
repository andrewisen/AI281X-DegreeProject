#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast

def readLines():
	file = "data.t3d"
	

	try:
		encoding='utf-16'
		fileObject = open(file,encoding=encoding)
	except Exception as e:
		#print("Error: File not loaded")
		pass
	try:
		encoding='ascii'
		fileObject = open(file,encoding=encoding)
	except Exception as e:
		#print("Error: File not loaded")
		pass


	lines = fileObject.read()
	splitlines = fileObject.read().splitlines()
	fileObject.close()

	return lines,splitlines

def main():
	lines, splitlines = readLines()

if __name__== "__main__":
	main()