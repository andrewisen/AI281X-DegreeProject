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
	objectDelta = {}
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
			tempA = metaDataBefore[metaDataHeader]
			tempB = metaDataAfter[metaDataHeader]

			if tempA == tempB:
				continue
			metaDataHeader, delta = calculateDifference(tempA,tempB,metaDataHeader,compareHeaders)
			objectDelta[metaDataHeader] = delta

			#print(metaDataHeader,delta)
		if bool(objectDelta) == False:
			continue 
		array[objectID] = objectDelta
		objectDelta = {}

	print(array)

def calculateDifference(tempA,tempB,metaDataHeader,compareHeaders):
	#print(metaDataHeader,tempA,tempB)

	intensity = compareHeaders[0]
	location = compareHeaders[1]
	rotation = compareHeaders[2]

	intensityDelta = ""
	locationDelta = []
	rotationDelta = []

	if metaDataHeader == intensity:
		intensityDelta = str(float(tempB) - float(tempA))
		return metaDataHeader,intensityDelta
	if metaDataHeader == location:
		coordinatesBefore = tempA.split(" ")
		coordinatesAfter = tempB.split(" ")

		for coordinate in range(3):
			coordinatesBefore[coordinate] = coordinatesBefore[coordinate].split("=")
			coordinatesAfter[coordinate] = coordinatesAfter[coordinate].split("=")
			
			locationBefore = float(coordinatesBefore[coordinate][1])
			locationAfter = float(coordinatesAfter[coordinate][1])
			delta = locationAfter - locationBefore
			delta = round(delta,2)
			locationDelta.append(str(delta))

		return metaDataHeader,locationDelta

	if metaDataHeader == rotation:
		coordinatesBefore = tempA.split(" ")
		coordinatesAfter = tempB.split(" ")

		for coordinate in range(3):
			coordinatesBefore[coordinate] = coordinatesBefore[coordinate].split("=")
			coordinatesAfter[coordinate] = coordinatesAfter[coordinate].split("=")
			
			locationBefore = float(coordinatesBefore[coordinate][1])
			locationAfter = float(coordinatesAfter[coordinate][1])
			delta = locationAfter - locationBefore
			delta = round(delta,2)
			rotationDelta.append(str(delta))
		return metaDataHeader,rotationDelta


	



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