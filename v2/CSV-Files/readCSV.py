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

def convertToDictionary(csvFile):
	headers = ["ID","Date","Intensity", "Location","Rotation"]
	objects = {}
	metaData = {}

	for line in csvFile:
		for _ in range(len(headers)):
			metaData[headers[_]] = line[_]
		objects[line[0]] = metaData
	
	return objects

def main():
	csvBefore,csvAfter,csvFileBefore,csvFileAfter = readCSV()

	csvDictBefore = convertToDictionary(csvBefore)
	csvDictAfter = convertToDictionary(csvAfter)

	#print(csvDictBefore)

	csvFileBefore.close()
	csvFileAfter.close()


	
if __name__== "__main__":
	main()