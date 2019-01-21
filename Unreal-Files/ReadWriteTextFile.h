// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "ReadWriteTextFile.generated.h"

/**
 * 
 */
UCLASS()
class LIGHTTEST_190117_API URWTxtFile : public UBlueprintFunctionLibrary
{
	GENERATED_BODY() public:

		UFUNCTION(BlueprintPure, Category = "Custom", meta = (Keywords = "LoadTxt"))
			static bool LoadTxt(FString FileNameA, FString& SaveTextA);

		// N.B: A BlueprintCallable function will have execution pins so that you can chain your C++ functions together in UE4 Blueprints.
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "SaveTxt"))
			static bool SaveTxt(FString SaveTextB, FString FileNameB);

		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "WriteTxt"))
			static bool SaveTxt(FString SaveTextB, FString FileNameB);

};
