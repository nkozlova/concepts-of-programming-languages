// TryCatchTrow.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include "TryCatchThrow.h"
#include <iostream>


void B() {
	std::cout << "Function B" << std::endl << "Throwing exception 0 from B" << std::endl;
	MY_THROW(TEST_EXCEPTION);
}

void A() {
	std::cout << "Function A" << std::endl;
	B();
}

void B(Object t) {
	Object t2;
	std::cout << "Throwing exception 0" << std::endl;
	MY_THROW(TEST_EXCEPTION);
}

void A(Object t) {
	Object t1;
	B(t);
}

int main() {
	MY_TRY(
		std::cout << "Throwing exception 1" << std::endl;
		MY_THROW(TEST_EXCEPTION_NEW);
	) MY_CATCH(TEST_EXCEPTION_NEW,
		std::cout << "Catching exception 1" << std::endl;
	) MY_END

	std::cout << std::endl;

	MY_TRY(
		std::cout << "Throwing exception 1" << std::endl;
		MY_THROW(TEST_EXCEPTION_NEW);
	) MY_CATCH(TEST_EXCEPTION,
		std::cout << "Catching exception 0" << std::endl;
	) MY_CATCH(TEST_EXCEPTION_NEW,
		std::cout << "Catching exception 1" << std::endl;
	) MY_END

	std::cout << std::endl;

	MY_TRY(
		MY_TRY(
			std::cout << "Throwing exception 1" << std::endl;
			MY_THROW(TEST_EXCEPTION_NEW);
		) MY_CATCH(TEST_EXCEPTION_NEW,
			std::cout << "Catching exception 1" << std::endl;
		) MY_END

		MY_TRY(
			std::cout << "Throwing exception 1" << std::endl;
			MY_THROW(TEST_EXCEPTION_NEW);
		) MY_CATCH(TEST_EXCEPTION_NEW,
			std::cout << "Catching exception 1" << std::endl;
		) MY_END

		A();

	) MY_CATCH(TEST_EXCEPTION,
		std::cout << "Catching exception 0" << std::endl;
	) MY_CATCH(TEST_EXCEPTION_NEW,
		std::cout << "Catching exception 1" << std::endl;
	) MY_END

	std::cout << std::endl;
	
	MY_TRY(
		MY_TRY(
			Object t1;
			Object t2;
			std::cout << "Throwing exception 1" << std::endl;
			MY_THROW(TEST_EXCEPTION_NEW);
			Object t3;
		) MY_CATCH(TEST_EXCEPTION,
			std::cout << "Catching exception 0" << std::endl;
		) MY_END

		std::cout << "Throwing exception 1" << std::endl;
		MY_THROW(TEST_EXCEPTION_NEW);
	) MY_CATCH(TEST_EXCEPTION_NEW,
		std::cout << "Catching exception 1" << std::endl;
	) MY_END
	
	std::cout << std::endl;
	
	MY_TRY(
		Object t1;
		Object t2;
		Object t3;
	) MY_CATCH(TEST_EXCEPTION,
		std::cout << "Catching exception 0" << std::endl;
	) MY_END

	std::cout << std::endl;

	MY_TRY(
		Object t;
		std::cout << "Throwing exception 0" << std::endl;
		MY_THROW(TEST_EXCEPTION);
	) MY_CATCH(TEST_EXCEPTION,
		std::cout << "Catching exception 0" << std::endl;
	) MY_END

	std::cout << std::endl;
	
	MY_TRY(
		Object t1;
		Object t2;
		Object t3;

		MY_TRY(
			Object t4;
			Object t5;
			Object t6;
			std::cout << "Throwing exception 0" << std::endl;
			MY_THROW(TEST_EXCEPTION);
		) MY_CATCH(TEST_EXCEPTION,
			std::cout << "Catching exception 0" << std::endl;
		) MY_END

	) MY_CATCH(TEST_EXCEPTION_NEW,
		std::cout << "Catching exception 1" << std::endl;
	) MY_END
	
	std::cout << std::endl;

	std::cout << "Exit" << std::endl;
    return 0;
}