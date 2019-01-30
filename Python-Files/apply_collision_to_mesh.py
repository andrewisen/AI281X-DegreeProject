import unreal
import csv

def GetCSV(csvPath):
	file = open(csvPath, "r")
	csvReader = csv.reader(file)
	csvList = list(csvReader)
	file.close()

	return csvList

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

	csvList = GetCSV(csvAbsPath)


	for i in csvList:
		print(i)

if __name__ == '__main__':
	main()