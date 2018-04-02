#pragma once
#include <stack>
#include <vector>
#include <iostream>


class Object {
	int num;

public:
	Object();

	int getNum();

	~Object() {}
};

class StackFrame {
public:
	void create_();
	void delete_();
};