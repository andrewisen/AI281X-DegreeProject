#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
def readCSV():
	fileBefore = "CSV_FileA.csv"
	fileAfter = "CSV_FileB.csv"
	delimiter = ";"
	try:
		csvBefore = open(fileBefore)
	except Exception as e:
		print("Error: File (before) not loaded")
		return
	try:
		csvAfter = open(fileAfter)
	except Exception as e:
		print("Error: File (after) not loaded")
		return

	csvBefore = csv.reader(csvBefore, delimiter=delimiter)
	csvAfter = csv.reader(csvAfter, delimiter=delimiter)
	
	return csvBefore,csvAfter


def main():
	csvBefore,csvAfter = readCSV()
	for i in csvBefore:
		print(i)

if __name__== "__main__":
	main()