#pragma once
#include <type_traits>
#include <string>
#include <set>
#include <map>


class TypeInfo 
{
	std::string nameOfClass;
	long hashCode;

public:
	TypeInfo(std::string name) : nameOfClass(name), hashCode(hash()) {}
	TypeInfo() : nameOfClass(""), hashCode(0) {}

	long hash() 
	{
		long res = 0, p = 54059;
		for (int i = 0; i < nameOfClass.size(); i++) {
			res += (static_cast<long>(pow(p, i)) * nameOfClass[i]);
		}
		return res;
	}

	std::string getName() { return nameOfClass; }

	long getHachCode() { return hashCode; }

	bool operator==(const TypeInfo &other) const {
		return other.nameOfClass == nameOfClass;
	}

	bool operator!=(const TypeInfo &other) const {
		return other.nameOfClass != nameOfClass;
	}
};


#define TYPEID(obj) \
	std::cout << "Name: " << obj->info.getName() << ", Hash: " << obj->info.getHachCode() << std::endl;