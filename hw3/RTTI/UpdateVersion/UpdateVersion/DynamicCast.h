#pragma once
#include "Class.h"

std::string typeNameOfClass, typeNameOfDestClass;

bool isTherePath(std::string NameOfClass, std::string NameOfToClass)
{
	return NameOfClass == NameOfToClass || parentsOfClasses[NameOfClass].find(NameOfToClass) != parentsOfClasses[NameOfClass].end();
}

#define DYNAMIC_CAST(DestTypeOfClass, obj, res) \
	typeNameOfClass = obj->realInfo.getName(); \
	typeNameOfDestClass = DestTypeOfClass::info.getName(); \
	if (isTherePath(typeNameOfClass, typeNameOfDestClass)) \
	{ \
		res = reinterpret_cast<DestTypeOfClass*>(obj); \
		res->realInfo = obj->realInfo; \
	} \
	else \
	{ \
		res = nullptr; \
	}