#!/usr/bin/env python
# -*- coding: utf-8 -*-

def readLines():
	fileName = "data.t3d"
	
	try:
		f = open(fileName,encoding='utf-16-le')
	except:
		return

	lines = f.read().splitlines() # Without n/
	#lines = f.readlines() # With n/

	f.close()

	return lines

def main():
	lines = readLines()
	
	for i in lines:
		print(i)

if __name__== "__main__":
	main()