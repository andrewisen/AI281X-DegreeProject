#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import re
import json
from marshmallow import Schema, fields, pprint


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
		self._metaData = "META DATA"
		self._location = "LOCATION DATA"
		#self._rotation = "ROTATION DATA"
		foo = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
		foo = json.dumps(foo)

		return {
		"ID":   self._ID,
		"MetaData": self._metaData,
		"Location": self._location,
		"Rotation": self._rotation,
		}

def readLines():
	# NB. Be aware of realtive or absolute path
	#file = "data.t3d" 
	file = "data.t3d" # DEV
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
					#pass
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

	try:
		for currentObject in specificObjects:
			for line in currentObject._object:
				if not metaDataString in line:
					continue	
				line = line.replace("(", "[").replace(")", "]")
				idx = line.find(metaDataString)
				line = line[idx + len(metaDataString):][1:-1]
				#line = json.dumps(line)
				line = ast.literal_eval(line)
				instanceMetaData = line

				currentObject.setMetaData(instanceMetaData)

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

				instanceLocation = line[idx:][1:-1]
				#.split(",")
				# E.g. ['X=19.890371', 'Y=150.939270', 'Z=218.699997']
				#instanceLocation.replace("[", "{").replace("]", "}")
				instanceLocation = "{" + instanceLocation + "}"
				currentObject.setLocation(instanceLocation)
	except Exception as e:
		print(e)
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
				instanceRotation = line[idx:][1:-1]
				#.split(",")
				# E.g. ['Pitch=0.000000', 'Yaw=89.999992', 'Roll=0.000000']
				instanceRotation = "{" + instanceRotation + "}"
				currentObject.setRotation(instanceRotation)
	except Exception as e:
		print("Error: Can't ger rotation")
	return rotation

def exportData(specificObjects):
	tempDict = {}



	for _ in range(len(specificObjects)):
		tempStr = json.dumps(specificObjects[_],default=specificObjects[_].serialize)
		#tempStr = tempStr[1:-1]
		tempStr = json.loads(tempStr)
		tempDict[str(_)] = tempStr

		#tempDict[str(_)] = specificObjects[_].serialize
		#print(specificObjects[_])

	
	#print(tempStr)
	#tempDict = json.dumps(tempDict.__dict__)
	print(tempDict)
	'''
		#_ = currentObject.serialize
		_ += json.dumps(currentObject,default=currentObject.serialize)[:-1] + ","
	_ = _[:-1] + "}"
	'''

	#with open("data.txt", "w") as file:
	#	json.dump(tempDict.__dict__,file)

	#print(_)


	#son.dumps(tempData)
	#simplejson.dumps(myObjInstance, default=MyObject.serialize)

	#jsonFile = []
	'''
	jsonFile = {}
	tempData = specificObjects[0]
	
	
	k = 0
	for currentObject in specificObjects:
		_ = json.dumps(currentObject.__dict__)
		jsonFile[k] = _
		k = k + 1
	with open("data.txt", "w") as file:
		json.dump(jsonFile,file)
	'''
class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()


class ObjectSchema(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema)


def marshmellowTest(specificObjects):
	dataTest = specificObjects[0]
	result = ObjectSchema().dump(dataTest)
	pprint(result)




def main():
	lines = readLines()
	objects = getObjects(lines)
	specificObjects = getSpecificObjects(objects)
	getMetaData(specificObjects)
	getLocation(specificObjects)
	getRotation(specificObjects)
	#exportData(specificObjects)

	marshmellowTest(specificObjects)
	


if __name__== "__main__":
	main()