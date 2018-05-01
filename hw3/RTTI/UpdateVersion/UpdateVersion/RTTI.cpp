#include <iostream>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <vector>
#include <math.h>

#include "TypeInfo.h"
#include "DynamicCast.h"
#include "Class.h"


CLASS(A, BaseParent)
END(A)

CLASS(B, A, BaseParent)
END(B)

CLASS(C, BaseParent)
END(C)

CLASS(D, A, B, C)
END(D)

CLASS(E, B, C)
END(E)

int main() 
{
	A *a = new A();
	B *b = new B();
	C *c = new C();
	D *d = new D();
	E *e = new E();

	TYPEID(a);
	TYPEID(b);
	TYPEID(c);
	TYPEID(d);
	TYPEID(e);

	std::cout << std::endl;
	std::cout << "a -> b : a " << a << std::endl;
	B *ab;
	DYNAMIC_CAST(B, a, ab);		// nullptr
	std::cout << "ab " << ab << std::endl;

	std::cout << std::endl;
	std::cout << "b -> a : b " << b << std::endl;
	A *ba;
	DYNAMIC_CAST(A, b, ba);
	std::cout << "ba " << ba << std::endl;

	std::cout << std::endl;
	std::cout << "a -> c : a " << a << std::endl;
	C *ac;
	DYNAMIC_CAST(C, a, ac);		// nullptr
	std::cout << "ac " << ac << std::endl;

	std::cout << std::endl;
	std::cout << "c -> a : c " << c << std::endl;
	A *ca;
	DYNAMIC_CAST(A, c, ca);		// nullptr
	std::cout << "ca " << ca << std::endl;

	std::cout << std::endl;
	std::cout << "c -> d : c " << c << std::endl;
	D *cd;
	DYNAMIC_CAST(D, c, cd);		// nullptr
	std::cout << "cd " << cd << std::endl;

	std::cout << std::endl;
	std::cout << "d -> a : d " << d << std::endl;
	A *da;
	DYNAMIC_CAST(A, d, da);
	std::cout << "da " << da << std::endl;

	std::cout << std::endl;
	std::cout << "c -> e : c " << c << std::endl;
	E *ce;
	DYNAMIC_CAST(E, c, ce);		// nullptr
	std::cout << "ce " << ce << std::endl;

	std::cout << std::endl;
	std::cout << "e -> a : e " << e << std::endl;
	A *ea;
	DYNAMIC_CAST(A, e, ea);
	std::cout << "ea " << ea << std::endl;
	
	system("pause");
	return 0;
}