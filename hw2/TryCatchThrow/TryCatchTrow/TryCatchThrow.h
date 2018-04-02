#pragma once
#include <setjmp.h>
#include "StackFrame.h"

// Список всех исключений
#define TEST_EXCEPTION 0
#define TEST_EXCEPTION_NEW 1

// Определяем максимальную вложенность исключений, если превысим этот порог -- завершаем работу
#define MAX_DEPTH 5

jmp_buf MY_EVENT[MAX_DEPTH];
int it = 0;
int exp_ = -1;
int value = 0;
StackFrame stack;

#define MY_TRY(doing) \
	value = 0; \
	if (it == MAX_DEPTH || exp_ != -1) exit(1); \
	stack.create_(); \
	value = setjmp(MY_EVENT[it++]); \
	if (value == 0 && exp_ == -1) { \
		doing; \
		--it; \
		stack.delete_(); \
	}

#define MY_THROW(exception) \
	if (exp_ != -1 || it <= 0) exit(1); \
	exp_ = exception; \
	stack.delete_(); \
	longjmp(MY_EVENT[--it], 1);

#define MY_CATCH(type_exception, doing) \
	else if (exp_ == type_exception) { \
		doing; \
		exp_ = -1; \
	}
