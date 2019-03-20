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

def convertToDictionary(csvFile,headers):
	objects = {}
	metaData = {}

	for line in csvFile:
		for _ in range(len(headers)):
			metaData[headers[_]] = line[_]
		objects[line[0]] = metaData
	
	return objects

def compareDictionaries(csvDictBefore,csvDictAfter,headers):

	if len(csvDictBefore) != len(csvDictAfter):
		print("Error: Dictionaries not equal lenght.")
		return

	for objectID in csvDictBefore:
		try:
			metaDataBefore = csvDictBefore[objectID]
			metaDataAfter = csvDictAfter[objectID]
		except Exception as e:
			print("Error: Can't open dictionaries.")
			print(e)
			return
		print(metaDataBefore)
		#for _ in range(1,len(csvDictBefore)):
		#	print(metaDataBefore[_])

def main():
	csvBefore,csvAfter,csvFileBefore,csvFileAfter = readCSV()

	headers = ["ID","Date","Intensity", "Location","Rotation"]
	csvDictBefore = convertToDictionary(csvBefore,headers)
	csvDictAfter = convertToDictionary(csvAfter,headers)

	compareDictionaries(csvDictBefore,csvDictAfter,headers)

	csvFileBefore.close()
	csvFileAfter.close()
	
if __name__== "__main__":
	main()