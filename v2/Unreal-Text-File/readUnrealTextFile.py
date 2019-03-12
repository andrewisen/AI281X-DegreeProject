#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import re
import json

class RevitObject:
	def __init__(self,instanceID,instanceObject):
		self._ID = instanceID
		self._object = instanceObject
		
		# Create empty lists, incase missing
		self._metaData = []
		self._location = []
		self._rotation = []

	def setMetaData(self,instanceMetaData):
		self._metaData = instanceMetaData

	def setLocation(self,instanceLocation):
		self._location = instanceLocation
	
	def setRotation(self,instanceRotation):
		self._rotation = instanceRotation

	def serialize(self,*arwg):
		#self._metaData = "META DATA"

		return {
			"ID":   self._ID,
			"MetaData": self._metaData,
			"Location": self._location,
			"Rotation": self._rotation,
		}

def readLines():
	#file = "data.t3d"
	file = "data_twoLights.t3d"
	
	try:
		fileObject = open(file,encoding='utf-16')
	except Exception as e:
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
		except Exception as e:
			print("Error: Can't append object")
	return objects

def getSpecificObjects(objects):
	specificObjects = []
	instanceID = ""

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
						instanceID = line
				idx = instanceID.find("=")
				instanceID = instanceID[idx + 2:][:-1]
				_ = RevitObject(instanceID,currentObject)
				specificObjects.append(_)				
	except Exception as e:
		print("Error: Can't get specific objects")
	return specificObjects

def getMetaData(specificObjects):
	metaDataString ="MetaData="
	metaData = {}

	try:
		for currentObject in specificObjects:
			for line in currentObject._object:
				if not metaDataString in line:
					continue	
				line = line.replace("(", "[").replace(")", "]")
				idx = line.find(metaDataString)
				line = line[idx + len(metaDataString):]
				line = ast.literal_eval(line)
				for _ in line:
					metaData[_[0]]= _[1]
				currentObject.setMetaData(metaData)
	except Exception as e:
		print("Error: Can't get MetaData" )
	return

def getLocation(specificObjects):
	locationString = "RelativeLocation=("
	location = {}

	try:
		for currentObject in specificObjects:
			for line in currentObject._object:
				if not locationString in line:
					continue
				idx = line.find("(")
				instanceLocation = line[idx:][1:-1].split(",")
				for axis in instanceLocation:
					key, value = axis.split("=")
					location[key] = value
				currentObject.setLocation(location)
	except Exception as e:
		print("Error: Can't get location")
	return location

def getRotation(specificObjects):
	rotationString = "RelativeRotation=("
	rotation = {}

	try:
		for currentObject in specificObjects:
			for line in currentObject._object:
				if not rotationString in line:
					continue
				idx = line.find("(")
				instanceRotation = line[idx:][1:-1].split(",")
				for axis in instanceRotation:
					key, value = axis.split("=")
					rotation[key] = value
				currentObject.setRotation(rotation)
	except Exception as e:
		print("Error: Can't ger rotation")
	return rotation

def exportData(specificObjects):
	tempDict = {}

	for _ in range(len(specificObjects)):
		tempStr = json.dumps(specificObjects[_],default=specificObjects[_].serialize)
		tempStr = json.loads(tempStr)
		tempDict["RevitObject" + str(_)] = tempStr

	with open("data.txt", "w") as file:
		json.dump(tempDict,file)

def main():
	lines = readLines()
	objects = getObjects(lines)
	specificObjects = getSpecificObjects(objects)
	getMetaData(specificObjects)
	getLocation(specificObjects)
	getRotation(specificObjects)
	
	exportData(specificObjects)

if __name__== "__main__":
	main()