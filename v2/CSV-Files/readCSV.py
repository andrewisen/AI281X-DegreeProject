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
	#metaData = {}


	for row in csvFile:
		metaData = {}
		for _ in range(len(headers)):
			metaData[headers[_]] = row[_]
		objects[row[0]] = metaData
		
	return objects

def compareDictionaries(csvDictBefore,csvDictAfter,headers):
	compareHeaders = headers[2:]
	array = {}
	#print(csvDictBefore)

	if len(csvDictBefore) != len(csvDictAfter):
		print("Error: Dictionaries not equal lenght.")
		return

	for objectID in csvDictBefore:
		try:
			metaDataBefore = csvDictBefore[objectID]
			metaDataAfter = csvDictAfter[objectID]
		except Exception as e:
			print("Error: Can't open dictionaries.")
			return
		for metaDataHeader in compareHeaders:
			A = metaDataBefore[metaDataHeader]
			B = metaDataAfter[metaDataHeader]

			if A == B:
				continue
	

			#print(A,end="\n\n")

			##continue


			#array[objectID] = [metaDataHeader,metaDataBefore[metaDataHeader],metaDataAfter[metaDataHeader]]

	#print(array)


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