#pragma once
#include "stdafx.h"
#include <iostream>

#include <map>


#define VIRTUAL_CLASS_DERIVED(NameOfStruct, NameOfBaseStruct) \
	struct NameOfStruct : public NameOfBaseStruct \
	{ \
		NameOfStruct() \
		{ \
			if (allMethods.find(#NameOfStruct) != allMethods.end()) \
			{ \
				methods = allMethods[#NameOfStruct]; \
			} \
			if (allMethods.find(#NameOfBaseStruct) != allMethods.end()) \
			{ \
				methods.insert(allMethods[#NameOfBaseStruct].begin(), allMethods[#NameOfBaseStruct].end()); \
			} \
		}

#define END_DERIVE(NameOfStruct, NameOfBaseStruct) \
	}; \
