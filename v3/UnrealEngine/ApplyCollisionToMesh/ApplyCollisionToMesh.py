import sys
import csv
import os

def ImportUnreal():
	try:
		import unreal               
	except ImportError:
		print('NB. The file must be run in Unreal Engine using "Python Editor Script Plugin".')
		sys.exit()

def GetAbsolutePath():
	absolutePath = os.path.realpath(__file__)


	return absolutePath


def GetCSV(csvPath):
	file = open(csvPath, "r")
	csvReader = csv.reader(file)
	csvList = list(csvReader)
	file.close()

	return csvList

def LoadAssets(assetPath):
	# Based on:
	# https://docs.unrealengine.com/en-us/Editor/Scripting-and-Automating-the-Editor/Editor-Scripting-How-Tos/Setting-up-Collision-Properties-in-Blueprints-and-Python

	# Get a list of all Assets in the path
	listOfAssets = unreal.EditorAssetLibrary.list_assets(assetPath)
	# Load them into memory
	assets = [unreal.EditorAssetLibrary.load_asset(eachAsset) for eachAsset in listOfAssets]

	return assets

def FilterAssets(csvList,assets):
	filteredAssets = []
	
	for idName in csvList:
		# Compare Revit assets with imported Unreal Assets
		# Maybe add funcitons for the last letters in Swedish

		idName = idName[0]
		idName = idName.replace(" ","_")
		idName = idName.replace(".","_")

		temporaryFinding = unreal.EditorFilterLibrary.by_id_name(assets, idName)
		if len(temporaryFinding) != 0:
			filteredAssets.append(temporaryFinding)

	return filteredAssets

def AddBoxCollision(staticMesh):
	# N.B. You could instead use: 
	# .SPHERE, .CAPSULE, N.DOP10_X, .NDOP10_Y, .NDOP10_Z, .NDOP18, .NDOP26
	shapeType = unreal.ScriptingCollisionShapeType.BOX
	
	unreal.EditorStaticMeshLibrary.add_simple_collisions(staticMesh, shapeType)
	unreal.EditorAssetLibrary.save_loaded_asset(staticMesh)

def main():
	ImportUnreal()
	### SET PATHS ###

	### Unreal Assets Path
	# N.B. The "Content" folder should be replaced with "Game".
	# Look at the info box when importing Datasmith Model.
	# Defualt: asset_path = "/Game/Revit/"
	assetPath = "/Game/Revit/"

	### CSV Path
	# Absolute Path 
	csvAbsPath = "" # Depricated
	# Relative Path  
	csvRelPath = "" # Depricated

	csvAbsPath = GetAbsolutePath()
	print(csvAbsPath)

	exit()

	### GET DATA ###
	# Get refrence items. Choose absolute or relative path as parameter
	csvList = GetCSV(csvAbsPath)
	# Get all items
	assets = LoadAssets(assetPath)

	### FILTER DATA ###
	filteredAssets = FilterAssets(csvList,assets)
	
	### ADD COLLISION ###
	for eachAsset in filteredAssets:
		map(AddBoxCollision, eachAsset)

if __name__ == '__main__':
	main()