#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import re

def readLines():
	# NB. Be aware of realtive or absolute path
	file = "data.t3d" 
	
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

	beginObjectPhrase = "Begin Actor"
	endObjectPhrase = "End Actor"

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
	specificObjects = []
	
	'''
	tags = [
			"0600x1200mm_4_Lamp__-_277V",
			"0600x1200mm_4_Lamp__-_277V",
			]
	'''

	tags = ["Revit.Instance.Id.362263"]

	for tag in tags:
		for currentObject in objects:
			if not any(tag in x for x in currentObject):
				continue
			specificObjects.append(currentObject)

	return specificObjects

def getMetaData(specificObjects):
	metaDataString ="MetaData="
	
	metaData = {}
	InstanceID = ""
	InstanceMetaData = ""

	regExString = 'ComponentTags...="Revit.Instance.Id'

	for currentObject in specificObjects:
		for line in currentObject:
			regEx = re.search(regExString, line)

			if (regEx):
				InstanceID = line
				continue
			elif not metaDataString in line:
				continue
			
			line = line.replace("(", "[").replace(")", "]")
			idx = line.find(metaDataString)
			line = line[idx + len(metaDataString):]

			line = ast.literal_eval(line)
			InstanceMetaData = line

		idx = InstanceID.find("=")
		InstanceID = InstanceID[idx + 2:][:-1]
		metaData[InstanceID] = InstanceMetaData
	return metaData

def getLocationAndRotation(specificObjects):
	location = {}
	rotation = {}

	for currentObject in specificObjects:
		for line in currentObject:
			print(line)


	return location, rotation
def main():
	lines = readLines()
	objects = getObjects(lines)
	specificObjects = getSpecificObjects(objects)
	metaData = getMetaData(specificObjects)
	location, rotation = getLocationAndRotation(specificObjects)
	

if __name__== "__main__":
	main()