import unreal
import csv

def GetCSV(csvPath):
	file = open(csvPath, "r")
	csvReader = csv.reader(file)
	csvList = list(csvReader)
	file.close()

	return csvList

def LoadAssets(assetPath):
	# Based on: 
	# https://docs.unrealengine.com/en-us/Editor/Scripting-and-Automating-the-Editor/Editor-Scripting-How-Tos/Setting-up-Collision-Properties-in-Blueprints-and-Python

	# Get a list of all Assets in the path.
	listOfAssets = unreal.EditorAssetLibrary.list_assets(assetPath)
	# Load them ll into memory.
	assets = [unreal.EditorAssetLibrary.load_asset(eachAsset) for eachAsset in listOfAssets]

	return assets

def FilterAssets(csvList,assets):
	filteredAssets = []
	
	for idName in csvList:
		idName = idName[0].replace(" ","_")
		temporaryFinding = unreal.EditorFilterLibrary.by_id_name(assets, idName)
		if len(temporaryFinding) != 0:
			filteredAssets.append(temporaryFinding)

	return filteredAssets

def main():
	''' SET PATHS '''

	### Unreal Assets Path
	# N.b. Content should be replaced with "Game".
	# Defualt: asset_path = "/Game/Revit/"
	assetPath = "/Game/Revit/190130_RevitCollisionScene_01/"

	### CSV Path
	# Absolute Path 
	csvAbsPath = "C:\\_DegreeProject-Spring19-AndreWisen\\190130 - Revit Collision\\ids.csv"
	# Relative Path to 
	csvRelPath = ""

	''' GET DATA '''
	# Get refrence items
	csvList = GetCSV(csvAbsPath)
	# Get all items
	assets = LoadAssets(assetPath)


	''' FILTER DATA '''
	filteredAssets = FilterAssets(csvList,assets)
	for i in filteredAssets:
		print(i)

if __name__ == '__main__':
	main()