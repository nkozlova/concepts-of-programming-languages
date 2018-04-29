#pragma once
#include "stdafx.h"
#include <iostream>

#include <functional>
#include <map>

std::map<std::string, std::map<std::string, std::function<void(void*)>>> allMethods = {};

#define VIRTUAL_CLASS(NameOfStruct) \
	struct NameOfStruct \
	{ \
		std::map<std::string, std::function<void(void*)>> methods; \
		NameOfStruct() \
		{ \
			if (allMethods.find(#NameOfStruct) != allMethods.end()) \
			{ \
				methods = allMethods[#NameOfStruct]; \
			} \
		} 		
		
#define END(NameOfStruct) \
	};

#define DECLARE_METHOD(NameOfStruct, nameOfMethod, whatToDo) \
	if (allMethods.find(#NameOfStruct) == allMethods.end()) \
	{ \
		allMethods.insert({#NameOfStruct, {}}); \
	} \
	allMethods[#NameOfStruct].insert({#nameOfMethod, [](void* obj) -> void { whatToDo }}); \
	

#define VIRTUAL_CALL(obj, nameOfMethod) \
	if (obj->methods.find(#nameOfMethod) != obj->methods.end()) \
	{ \
		obj->methods[#nameOfMethod]((void*)obj); \
	}

#define CAST(NameOfStructTo, obj, res) \
	res = reinterpret_cast<NameOfStructTo*>(&obj); \
	std::map<std::string, std::function<void(void*)>> methodsCopy; \
	for (auto it : res->methods) \
	{ \
		if (allMethods[#NameOfStructTo].find(it.first) != allMethods[#NameOfStructTo].end()) \
		{ \
			methodsCopy.insert(it); \
		} \
	} \
	res->methods = methodsCopy; \
