#pragma once
#include "stdafx.h"


#include <functional>
#include <map>


#define VIRTUAL_CLASS(NameOfStruct) \
	struct NameOfStruct \
	{ \
		static std::map<std::string, std::function<void(void*)>> methods; \
		static void addMethod(std::string nameOfMethod, std::function<void(void*)> method) \
		{ \
			NameOfStruct::methods.insert({ nameOfMethod, method }); \
		} \
		static std::map<std::string, std::function<void(void*)>> methodsCasting; \
		bool flagCasting;

#define END(NameOfStruct) \
	}; \
	std::map<std::string, std::function<void(void*)>> NameOfStruct::methods = {}; \
	std::map<std::string, std::function<void(void*)>> NameOfStruct::methodsCasting = {};

#define DECLARE_METHOD(NameOfStruct, nameOfMethod, whatToDo) \
	NameOfStruct::addMethod(#nameOfMethod, [](void* obj) -> void { whatToDo });

#define VIRTUAL_CALL(obj, nameOfMethod) \
	if (obj->flagCasting && obj->methodsCasting.find(#nameOfMethod) != obj->methodsCasting.end()) \
	{ \
		obj->methodsCasting[#nameOfMethod]((void*)obj); \
	} else \
	{ \
		obj->methods[#nameOfMethod]((void*)obj); \
	}


