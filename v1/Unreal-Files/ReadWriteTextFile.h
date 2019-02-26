/**
* Credit: https://answers.unrealengine.com/questions/120392/how-can-i-load-text-from-file-with-blueprint.html
*
* See UE4s docs for more infromation about FFileHelper
* https://api.unrealengine.com/INT/API/Runtime/Core/Misc/FFileHelper/SaveStringToFile/index.html
*/

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "ReadWriteTextFile.generated.h"

// Unreal Engine 4
UCLASS()
class LIGHTTEST_190117_API URWTxtFile : public UBlueprintFunctionLibrary
{
	GENERATED_BODY() public:

		// Get value (string) from text file (relative path)
		UFUNCTION(BlueprintPure, Category = "Custom", meta = (Keywords = "LoadTxt"))
			static bool LoadTxt(FString FileNameA, FString& SaveTextA);

		// Set value (string) to text file (relative path)
		// A BlueprintCallable function will have execution pins so that you can chain your C++ functions together in UE4 Blueprints.
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "SaveTxt"))
			static bool SaveTxt(FString SaveTextB, FString FileNameB);

		// Set value (string) to text file (absolute path)
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "WriteTxt"))
			static bool WriteTxt(FString SaveTextB, FString FileNameB);

};
