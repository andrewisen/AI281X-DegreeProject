#!/usr/bin/env python
# -*- coding: utf-8 -*-
def openFile():
	file = open("text.txt", "w")

	file.write("New line") 

	file.close()

def main():
	openFile()

if __name__== "__main__":
	main()

