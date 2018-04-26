#pragma once
#include "stdafx.h"

#include <map>


#define VIRTUAL_CLASS_DERIVED(NameOfStruct, NameOfBaseStruct) \
	struct NameOfStruct : public NameOfBaseStruct \
	{ \
		static std::map<std::string, std::function<void(void*)>> methods; \
		static void addMethod(std::string nameOfMethod, std::function<void(void*)> method) \
		{ \
			NameOfStruct::methods.insert({ nameOfMethod, method }); \
			if (NameOfBaseStruct::methods.find(nameOfMethod) != NameOfBaseStruct::methods.end()) \
			{ \
				methodsCasting.insert({ nameOfMethod, method }); \
			} \
		}

#define END_DERIVE(NameOfStruct, NameOfBaseStruct) \
	}; \
	std::map<std::string, std::function<void(void*)>> NameOfStruct::methods = {};//NameOfBaseStruct::methods;

#define CAST(obj) \
	obj->flagCasting = true;