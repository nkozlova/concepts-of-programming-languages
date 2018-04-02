#include "stdafx.h"
#include "StackFrame.h"


int count = 0;

// Стэк всех объектов по уровням (на i-м try i-й вектор объектов стэка)
std::stack<std::vector<Object*>> objects;

Object::Object() : num(count++) {
	std::cout << "Create object " << num << std::endl;
	if (objects.empty()) {
		objects.emplace();
	}
	objects.top().push_back(this);
}

int Object::getNum() {
	return num;
}

void StackFrame::create_() {
	objects.emplace();
}

void StackFrame::delete_() {
	if (objects.empty()) {
		return;
	}

	for (auto obj : objects.top()) {
		std::cout << "Destroy object " << obj->getNum() << std::endl;
		obj->~Object();
	}
	objects.pop();
}