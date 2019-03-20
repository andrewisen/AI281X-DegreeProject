#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json

def readCSV(fileFilePathBefore,fileFilePathAfter,delimiter):
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
			tempMetaDataBefore = metaDataBefore[metaDataHeader]
			tempMetaDataAfter = metaDataAfter[metaDataHeader]

			if tempMetaDataBefore == tempMetaDataAfter:
				continue
			metaDataHeader, delta = calculateDifference(tempMetaDataBefore,tempMetaDataAfter,metaDataHeader,compareHeaders)
			objectDelta[metaDataHeader] = delta

		if bool(objectDelta) == False:
			continue 
		array[objectID] = objectDelta
		objectDelta = {}
	return array

def calculateDifference(tempMetaDataBefore,tempMetaDataAfter,metaDataHeader,compareHeaders):
	intensity = compareHeaders[0]
	location = compareHeaders[1]
	rotation = compareHeaders[2]

	intensityDelta = ""
	locationDelta = []
	rotationDelta = []

	if metaDataHeader == intensity:
		intensityDelta = str(float(tempMetaDataAfter) - float(tempMetaDataBefore))
		return metaDataHeader,intensityDelta
	if metaDataHeader == location:
		coordinatesBefore = tempMetaDataBefore.split(" ")
		coordinatesAfter = tempMetaDataAfter.split(" ")

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
		coordinatesBefore = tempMetaDataBefore.split(" ")
		coordinatesAfter = tempMetaDataAfter.split(" ")

		for coordinate in range(3):
			coordinatesBefore[coordinate] = coordinatesBefore[coordinate].split("=")
			coordinatesAfter[coordinate] = coordinatesAfter[coordinate].split("=")
			
			locationBefore = float(coordinatesBefore[coordinate][1])
			locationAfter = float(coordinatesAfter[coordinate][1])
			delta = locationAfter - locationBefore
			delta = round(delta,2)
			rotationDelta.append(str(delta))
		return metaDataHeader,rotationDelta

def exportData(array):
	
	my_dict = json.dumps(array)
	with open("deltaOut.txt", "w") as file:
		file.write(my_dict)

def main():
	# === SETTINGS ===
	fileFilePathBefore = "CSV_FileA.csv"
	fileFilePathAfter = "CSV_FileB.csv"
	delimiter = ";"
	headers = ["ID","Date","Intensity", "Location","Rotation"] # Hard coding

	# === OPEN FILES ===
	csvBefore,csvAfter,csvFileBefore,csvFileAfter = readCSV(fileFilePathBefore,fileFilePathAfter,delimiter)

	# === READ FILE ===
	csvDictBefore = convertToDictionary(csvBefore,headers)
	csvDictAfter = convertToDictionary(csvAfter,headers)


	array = compareDictionaries(csvDictBefore,csvDictAfter,headers)
	exportData(array)
	# === OPEN FILES ===
	csvFileBefore.close(), csvFileAfter.close()
	
if __name__== "__main__":
	main()