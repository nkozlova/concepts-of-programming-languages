#pragma once
#include "TypeInfo.h"


std::map<std::string, std::set<std::string>> parentsOfClasses;	// Каждому классу ставится в соответствие все его родители

void convertString(std::string str, std::set<std::string> &resultSet)
{
	str = str.substr(1, str.length() - 2);
	if (str.length() != 0)
	{
		int pos = 0;
		while (pos != std::string::npos)
		{
			pos = str.find(",");
			std::string curStr = str.substr(0, pos);
			if (int spacePos = curStr.find(" ") != std::string::npos)
			{
				curStr = curStr.substr(spacePos);
			}
			if (curStr != "BaseParent")
			{
				resultSet.insert(curStr);
			}
			str = str.substr(pos + 1);
		}
	}
}

void addClass(std::string NameOfFromClass, std::string NameOfToClasses)
{
	std::set<std::string> to;
	convertString(NameOfToClasses, to);

	parentsOfClasses.insert({ NameOfFromClass, {} });

	parentsOfClasses[NameOfFromClass] = to;
	for (auto parent : to)
	{
		for (auto parentOfParent : parentsOfClasses[parent])
		{
			parentsOfClasses[NameOfFromClass].insert(parentOfParent);
		}
	}
}

class BaseParent	// Базовый класс, от которого будут наследоваться все остальные
{
public:
	BaseParent() {}
};

#define RET_SHARP(x) #x

#define CLASS(NameOfClass, ...) \
class NameOfClass : public __VA_ARGS__ \
{ \
public: \
	static TypeInfo info; \
	TypeInfo realInfo; \
	NameOfClass() \
	{ \
		realInfo = TypeInfo(#NameOfClass); \
		if (parentsOfClasses.find(#NameOfClass) == parentsOfClasses.end()) \
		{ \
			addClass(#NameOfClass, RET_SHARP((__VA_ARGS__))); \
		} \
	}

#define END(NameOfClass) \
}; \
TypeInfo NameOfClass::info = TypeInfo(#NameOfClass);
