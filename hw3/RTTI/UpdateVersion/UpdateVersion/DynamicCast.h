#pragma once
#include "Class.h"

std::string typeNameOfClass, typeNameOfDestClass;

bool isTherePath(std::string NameOfClass, std::string NaemOfToClass)
{
	return parentsOfClasses[NameOfClass].find(NaemOfToClass) != parentsOfClasses[NameOfClass].end();
}

#define DYNAMIC_CAST(DestTypeOfClass, obj, res) \
	typeNameOfClass = obj->info.getName(); \
	typeNameOfDestClass = DestTypeOfClass::info.getName(); \
	if (isTherePath(typeNameOfClass, typeNameOfDestClass)) \
	{ \
		res = reinterpret_cast<DestTypeOfClass*>(obj); \
	} \
	else \
	{ \
		res = nullptr; \
	}