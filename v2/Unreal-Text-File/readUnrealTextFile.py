#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import re

def readLines():
	# NB. Be aware of realtive or absolute path
	# file = "data.t3d" 
	file = "data_rotate.t3d" # DEV
	
	try:
		fileObject = open(file,encoding='utf-16')
	except:
		print("Error: File not loaded")
		return

	lines = fileObject.read().splitlines()
	fileObject.close()

	return lines

def getObjects(lines):
	#beginObjectPhrase = "Begin Object"
	#endObjectPhrase = "End Object"

	beginObjectPhrase = "Begin Actor" # DEV
	endObjectPhrase = "End Actor" # DEV

	status = "end"
	objects = []
	currentObject = []

	for line in lines:	
		if beginObjectPhrase in line: 
			status = "begin"
			pass
		elif endObjectPhrase in line: 
			status = "end"
			objects.append(currentObject)
			currentObject = []
			continue
		elif status == "begin":
			pass
		elif status == "end":
			continue
		try:
			currentObject.append(line)
		except:
			print("Error: Can't append object")
	return objects

def getSpecificObjects(objects):
	specificObjects = {}
	'''
	tags = [
			"0600x1200mm_4_Lamp__-_277V",
			"0600x1200mm_4_Lamp__-_277V",
			]
	'''

	tags = ["Revit.Instance.Id.362263"] # DEV
	regExString = 'ComponentTags...="Revit.Instance.Id'

	try:
		for tag in tags:
			for currentObject in objects:
				if not any(tag in x for x in currentObject):
					continue
				for line in currentObject:
					regEx = re.search(regExString, line)
					if (regEx):
						InstanceID = line
				idx = InstanceID.find("=")
				InstanceID = InstanceID[idx + 2:][:-1]
				specificObjects[InstanceID] = currentObject
				# E.g. {'Revit.Instance.Id.362263': ["..."],'Revit.Instance.Id.365463': ["..."]}
	except:
		print("Error: Can't get specific objects")
	return specificObjects

def getMetaData(specificObjects):
	metaDataString ="MetaData="
	metaData = {}

	try:
		for instanceID, currentObject in specificObjects.items():
			for line in currentObject:
				if not metaDataString in line:
					continue	
				line = line.replace("(", "[").replace(")", "]")
				idx = line.find(metaDataString)
				line = line[idx + len(metaDataString):]
				line = ast.literal_eval(line)
				instanceMetaData = line
			metaData[instanceID] = instanceMetaData
	except:
		print("Error: Can't get MetaData" )
	return metaData

def getLocation(specificObjects):
	locationString = "RelativeLocation=("
	location = {}

	try:
		for instanceID, currentObject in specificObjects.items():
			for line in currentObject:
				if not locationString in line:
					continue
				idx = line.find("(")
				instanceLocation = line[idx:][1:-1].split(",")
				# E.g. ['X=19.890371', 'Y=150.939270', 'Z=218.699997']
			location[instanceID] = instanceLocation
	except:
		print("Error: Can't get location")
	return location

def getRotation(specificObjects):
	rotationString = "RelativeRotation=("
	rotation = {}

	try:
		for instanceID, currentObject in specificObjects.items():
			for line in currentObject:
				if not rotationString in line:
					continue
				idx = line.find("(")
				instanceRotation = line[idx:][1:-1].split(",")
				# E.g. ['Pitch=0.000000', 'Yaw=89.999992', 'Roll=0.000000']
			rotation[instanceID] = instanceRotation
	except:
		print("Error: Can't ger rotation")
	return rotation

def main():
	lines = readLines()
	objects = getObjects(lines)
	specificObjects = getSpecificObjects(objects)
	metaData = getMetaData(specificObjects)
	location = getLocation(specificObjects)
	rotation = getRotation(specificObjects)

if __name__== "__main__":
	main()