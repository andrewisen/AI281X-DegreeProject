// EU4 Test Class

#include "ReadWriteTextFile.h"

bool URWTxtFile::LoadTxt(FString FileNameA, FString& SaveTextA)
{
	return FFileHelper::LoadFileToString(SaveTextA, *(FPaths::GameDir() + FileNameA));
}

bool URWTxtFile::SaveTxt(FString SaveTextB, FString FileNameB)
{
	return FFileHelper::SaveStringToFile(SaveTextB, *(FPaths::GameDir() + FileNameB));
}


bool URWTxtFile::WriteTxt(FString SaveTextB, FString FileNameB)
{
	// https://api.unrealengine.com/INT/API/Runtime/Core/Misc/FFileHelper/SaveStringToFile/index.html
	return FFileHelper::SaveStringToFile(SaveTextB, *(FileNameB));
}

