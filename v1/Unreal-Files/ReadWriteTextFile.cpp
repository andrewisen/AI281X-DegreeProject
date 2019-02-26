/**
* Credit: https://answers.unrealengine.com/questions/120392/how-can-i-load-text-from-file-with-blueprint.html
* 
* See UE4s docs for more infromation about FFileHelper
* https://api.unrealengine.com/INT/API/Runtime/Core/Misc/FFileHelper/SaveStringToFile/index.
*/

#include "ReadWriteTextFile.h"

// Get value (string) from text file (relative path)
bool URWTxtFile::LoadTxt(FString FileNameA, FString& SaveTextA)
{
	return FFileHelper::LoadFileToString(SaveTextA, *(FPaths::GameDir() + FileNameA));
}

// Set value (string) to text file (relative path)
bool URWTxtFile::SaveTxt(FString SaveTextB, FString FileNameB)
{
	return FFileHelper::SaveStringToFile(SaveTextB, *(FPaths::GameDir() + FileNameB));
}

// Set value (string) to text file (absolute path)
bool URWTxtFile::WriteTxt(FString SaveTextB, FString FileNameB)
{
	return FFileHelper::SaveStringToFile(SaveTextB, *(FileNameB));
}