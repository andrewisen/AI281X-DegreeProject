#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import sys

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
	splitlines = lines.splitlines()
	fileObject.close()

	return lines,splitlines

def replaceDoubleQuoutes(lines):
	array = []
	for line in lines:
		#line = line.replace('"','\"')
		line = line.replace('"','---')
		array.append(line)
	return array

def addSeperator(lines):
	searchStringWithSpace = "Begin "
	searchString = "Begin"

	for line in lines:
		if searchStringWithSpace not in line:
			continue

		words = line.split(" ") 
		

		searchStringIndex = words.index(searchString)
		seperatorWord = words[searchStringIndex]
		seperatorWord = '"' + seperatorWord
		words[searchStringIndex] = seperatorWord

		words[-1] = words[-1] + '"'

		print(words)


def main():
	lines, splitlines = readLines()
	# Lines is a string
	# Splitlines is a list containing each row

	lines = splitlines

	lines = replaceDoubleQuoutes(lines)
	addSeperator(lines)


if __name__== "__main__":
	main()