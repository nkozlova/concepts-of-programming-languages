// OOP.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"

#include "BaseStructure.h"
#include "DerivedStructure.h"


// базовый класс
VIRTUAL_CLASS(Base)
	int a = 0;
END(Base)

// класс-наследник
VIRTUAL_CLASS_DERIVED(Derived, Base)
	int b = 0;
END_DERIVE(Derived, Base)

	
int main()
{
	// методы
	DECLARE_METHOD(Base, Both, { std::cout << "Base::Both a = " << ((Base*)obj)->a << std::endl; })
	DECLARE_METHOD(Base, OnlyBase, { std::cout << "Base::onlyBase" << std::endl; })
	
	DECLARE_METHOD(Derived, Both, { std::cout << "Derived::Both b = " << ((Derived*)obj)->b << std::endl; })
	DECLARE_METHOD(Derived, OnlyDerived, { std::cout << "Derived::OnlyDerived" << std::endl; })
	

	Base base;
	base.a = 0;

	Derived derived;
	derived.b = 1;

	Base *reallyDerived;
	CAST(Base, derived, reallyDerived);

	VIRTUAL_CALL((&derived), Both);

	VIRTUAL_CALL((&base), Both); // печатает "Base::Both a = 0"
	VIRTUAL_CALL((&base), OnlyBase);	// печатает "Base::OnlyBase"
	VIRTUAL_CALL((&base), OnlyDerived);	// печатает "Base::OnlyBase"


	VIRTUAL_CALL(reallyDerived, Both); // печатает "Derived::Both b = 1"
	VIRTUAL_CALL(reallyDerived, OnlyBase);  // печатает "Base::OnlyBase"
	VIRTUAL_CALL(reallyDerived, OnlyDerived);  
	return 0;
}