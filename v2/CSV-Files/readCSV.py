#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
def readCSV():
	fileFilePathBefore = "CSV_FileA.csv"
	fileFilePathAfter = "CSV_FileB.csv"
	delimiter = ";"
	try:
		csvFileBefore = open(fileFilePathBefore)
	except Exception as e:
		print("Error: File (before) not loaded.")
		return
	try:
		csvFileAfter = open(fileFilePathAfter)
	except Exception as e:
		print("Error: File (after) not loaded.")
		return

	csvBefore = csv.reader(csvFileBefore, delimiter=delimiter)
	csvAfter = csv.reader(csvFileAfter, delimiter=delimiter)


	return csvBefore,csvAfter,csvFileBefore,csvFileAfter


def main():
	csvBefore,csvAfter,csvFileBefore,csvFileAfter = readCSV()
	for i in csvBefore:
		print(i)

	csvFileBefore.close()
	csvFileAfter.close()
	
if __name__== "__main__":
	main()